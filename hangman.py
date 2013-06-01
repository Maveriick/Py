# Rudimentary Hangman Game Implementation

class hangmanObject:
    'This is the object for Hang Man Game'
    def __init__(self,char,found):
        self.Character = char
        self.Found = found

def printSeq(inputList):
    for eachItem in inputList:
        if eachItem.Found == 0:
            print eachItem.Character,
        else:
            print "_ ",
    print "\n"

def update(guess,objectList):
    global toGuess
    global chances

    exist = 1
        
    x = toGuess
    for eachItem in objectList:
        if eachItem.Character == guess and eachItem.Found == 1:
            eachItem.Found = 0
            toGuess -= 1
            exist = 0
    if x == toGuess:
        chances-=1
        
def main():
    global toGuess
    global chances
    global chosen
    objectList = []
    movie = raw_input("Please enter the name of the movie:")
    inputList = list(movie)
    toGuess = len(movie)
    for eachItem in inputList:
        newObj = hangmanObject(eachItem, 1)
        objectList.append(newObj)
    printSeq(objectList)
    done = 0
    chances = 4
    chosen = ""
    while not done:
        if chances == 0:
            print "You lost",
            print "Have a good day"
            print movie
            break
        
        if toGuess == 0:
            print "You succeeded"
            print "Have a good day"
            break
        
        
        guess = raw_input("Please Enter your character guess:")
        update(guess,objectList)
        printSeq(objectList)
        print "Chances Remaining: " + str(chances)
        
        
        


    
        
