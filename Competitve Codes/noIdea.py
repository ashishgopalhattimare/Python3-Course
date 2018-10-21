if __name__ == '__main__':
    inp = input().split(" ")
    
    n = int(inp[0])
    m = int(inp[1])
    
    # array of n input
    nums = map(int, input().split(" "))
    
    A = map(int, input().split(" "))
    setA = set(A)
    
    B = map(int, input().split(" "))
    setB = set(B)
    
    happiness = 0
    for x in nums:
        if x in setA:
            happiness+=1
        if x in setB:
            happiness-=1
    
    print (happiness)