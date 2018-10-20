def generateWord(word, start, end):
    
    if start == end:
        print word
    
    else:
        for i in range(start, end+1):
            word[i], word[start] = word[start], word[i]
            generateWord(word, start+1, end)
            word[i], word[start] = word[start], word[i]

if __name__ == '__main__':
    
    word = ['a','c','d','g','o','t']
    generateWord(word, 0, len(word)-1)