if __name__ == '__main__':
    
    wordDict = {} # dictionary
    wordList = [] # list
    for _ in range(int(input())):
        word = input()
        
        if word not in wordDict:
            wordList.append(word)
            wordDict[word] = 0
        wordDict[word]+=1
    
    print (len(wordList))
    for x in wordList:
        print (wordDict[x], end=" ")
    print ()