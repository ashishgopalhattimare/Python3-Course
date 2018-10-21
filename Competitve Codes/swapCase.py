def swap_case(s):
    word = list(s)
    
    for i in range(len(word)):
        if word[i] == word[i].upper():
            word[i] = word[i].lower()
        else:
            word[i] = word[i].upper()
        
    return "".join(word)
    
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)