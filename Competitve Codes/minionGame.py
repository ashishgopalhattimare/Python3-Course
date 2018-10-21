def minion_game(string):
    # your code goes here
    
    stuartDict = {}
    kevinDict = {}
    
    kevinCount = 0
    stuartCount = 0
    
    for i in range(len(string)):
        if string[i] not in ['A','E','I','O','U']:
            stuartCount += (len(string)-i)
                
    for i in range(len(string)):
        if string[i] in ['A','E','I','O','U']:
            kevinCount += (len(string)-i)
        
    if stuartCount > kevinCount:
        print ("Stuart",stuartCount)
    elif stuartCount < kevinCount:
        print ("Kevin",kevinCount)
    else:
        print ("Draw")
        
if __name__ == '__main__':
    s = input()
    minion_game(s)