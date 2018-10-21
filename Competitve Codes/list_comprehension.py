current = [0,0,0]
result = []

def algorithm(index, nums, n, sum):
    if index == 3:
        if sum != n:
            # append new copy of the list
            # as object are stored in the result
            
            # changing one would update the rest
            result.append(list(current))
        return
    
    for i in range(nums[index]+1):
        current[index]+=i
        algorithm(index+1, nums, n, sum+i)
        current[index]-=i
        
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    algorithm(0, [x, y, z], n, 0)
        
    print (result)