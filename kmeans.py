#!/usr/bin/env
import sys
import random
import math

class Mean:
    '__class__Mean__'
    def __init__(self,x_Cordinate,y_Cordinate):
        self.xCord = x_Cordinate
        self.yCord = y_Cordinate
    
    def printData(self):
        print "Mean\n"
        print "X Cord: " + str(self.xCord)
        print "Y Cord: " + str(self.yCord)
        print "\n"

    
        

class Point:
    '__class__Point__'
    def __init__(self,x_Cordinate,y_Cordinate,cluster_Num = 0):
        self.xCord = x_Cordinate
        self.yCord = y_Cordinate
        self.clusterNum = cluster_Num

    def printData(self):
        print "Point\n"
        print "X Cord: " + str(self.xCord)
        print "Y Cord: " + str(self.yCord)
        print "Cluster Num : " + str(self.clusterNum)
        print "\n"

    

    


def readFile(filename):
    pointList = []
    fileHandler = open(filename,'r')
    for line in fileHandler:
        line = line.rstrip("\n")
        tempList = line.split(",")
        print tempList
        tempPoint = Point(tempList[0],tempList[1],0)
        pointList.append(tempPoint)
    return pointList

def printPointList(pointList):
    for eachItem in pointList:
        print eachItem.xCord,
        print eachItem.yCord,
        print eachItem.clusterNum,
        print "\n"

def printMedianList(medianList):
    print "Medians\n"
    for eachItem in medianList:
        print eachItem.xCord,
        print eachItem.yCord,
        print "\n"

def getMins(pointList):
    xCords = []
    yCords = []
    for eachItem in pointList:
        xCords.append(eachItem.xCord)
        yCords.append(eachItem.yCord)
    xCords = sorted(xCords)
    yCords = sorted(yCords)
    return xCords[0],xCords[len(xCords) - 1],yCords[0],yCords[len(yCords) - 1]

def generateMeans(givenClusters,xMin,yMin,xMax,yMax):
    global meanList
    meanList = []
    count = 0
    while count != givenClusters:
        isThere = 0
        xRand = random.randint(int(xMin),int(xMax))
        yRand = random.randint(int(yMin),int(yMax))
        tempMean = Mean(xRand,yRand)
        meanList.append(tempMean)
        count += 1    
    return meanList


def euclidDistance(point,mean):
    xdiff = (int(point.xCord) - int(mean.xCord))**2
    ydiff = (int(point.yCord) - int(mean.yCord))**2
    diff = math.sqrt(xdiff + ydiff)
    return diff

def calculateMean(pointList):
    xSum = 0
    ySum = 0
    for eachPoint in pointList:
        xSum = int(xSum) + int(eachPoint.xCord)
        ySum = int(ySum) + int(eachPoint.yCord)
    newMean = Mean(xSum/len(pointList),ySum / len(pointList))
    return newMean

def reCalculateMean(pointList,givenNumber):
    cluster = [[] for x in range(givenNumber)]
    newMeans = []
    count = 0
    for eachPoint in pointList:
        num = eachPoint.clusterNum
        tempMean = Mean(eachPoint.xCord,eachPoint.yCord)
        cluster[num-1].append(tempMean)
       
    for eachCluster in cluster:
        #printMedianList(eachCluster)
        tempMean = calculateMean(eachCluster)
        newMeans.append(tempMean)
        
    #printMedianList(newMeans)
    return newMeans

def checkMeanChange(oldMeans,newMeans):
    if(len(oldMeans) != len(newMeans)):
       return 1

    if (len(oldMeans) == len(newMeans)):
        for x in range(len(newMeans)):
            oldObject = oldMeans[x]
            newObject = newMeans[x]
            if oldObject.xCord == newObject.xCord and oldObject.yCord == newObject.yCord:
                pass
            else:
                return 1
    return 0

        

def clusterify(pointList,meansList):
        
    newMeans = meansList
    count = 0
    while(checkMeanChange(newMeans,meansList) != 1):
        for eachPoint in pointList:
            count = 0
            minDist = float('inf')
            #eachPoint.printData()
            for eachMean in meansList:
                    #print eachMean.printData()
                    dist = euclidDistance(eachPoint,eachMean)
                    #print "Dist: " + str(dist)
                    if dist < minDist:
                        minDist = dist
                        count += 1
            eachPoint.clusterNum = count
        meanList = newMeans
        newMeans = reCalculateMean(pointList,len(meansList))
        #printMedianList(newMeans)
    
    printPointList(pointList)
    
    

def init(pointList,givenNumber):
    #get the Min,Max for x and y co-ordinates in order to generate Medians in the range
    [xMin,xMax,yMin,yMax] = getMins(pointList)

    #generate the means
    meansList = generateMeans(givenNumber,xMin,xMax,yMin,yMax)
    clusterify(pointList,meansList)


        



            
def main():
    
    #get the system argument for filename
    inputFile = sys.argv[1]

    #get the number of clusters
    givenClusters = sys.args[2]
    init(inputFile,givenClusters)
        
 

    
    #init(pointList,2)

    

    


    
    


    
            



if __name__ == "__main__":
    main()
