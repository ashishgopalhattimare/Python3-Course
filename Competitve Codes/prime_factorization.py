def get_num(arr):
    # your code here
    
    actualNum = 1
    for x in arr:
        actualNum *= x
    
    factor = 2
    small, large, count = 0, 0, 1
    
    while factor+factor <= actualNum:
        if actualNum % factor == 0:
            if small == 0:
                small = factor
            large = factor
            count+=1
        factor+=1
    
    return [actualNum, count, small, large]
    
if __name__ == '__main__':
    print (get_num([2,3,5,5])
    print (get_num([2,13,2,5,2,5,3,3]))