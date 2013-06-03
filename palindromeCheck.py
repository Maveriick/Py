def palindromeCheck(stringOne):
    

    if len(stringOne) == 0:
        return True
    else:
        begin = 0
        end = len(stringOne) - 1
        while begin < end :
            #print begin
            #print end
            #print "\n"
            if stringOne[begin] == stringOne[end]:
                begin+=1
                end-=1
            else:
                return False
        return True


def main():
    
        
    assert (palindromeCheck("abccba") == True),"Correct"
    assert (palindromeCheck("abca") != True),"Correct"
    assert(palindromeCheck("abcba") == True),"Correct"
    assert(palindromeCheck("abcdcba") == True),"Correct"
    assert(palindromeCheck("abcdedcba") == True),"Correct"
        
                       
