from math import *

def minmax(nums):
    minim, maxim = nums[0], nums[0]
    
    for i in range(len(nums)):
        minim = min(minim, nums[i])
        maxim = max(maxim, nums[i])

    return minim, maxim
    
if __name__ == '__main__':
    nums = [1,5,7,123,76,23,-432,657,12,-1,-32,123]
    
    minim, maxim = minmax(nums)
    print nums
    print 'Minimum and Maximum in the list is :',minim,maxim