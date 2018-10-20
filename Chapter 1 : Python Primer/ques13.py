def reverseList(nums):
    start, end = 0, len(nums)-1
    
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start+=1
        end-=1

if __name__ == '__main__':
    
    nums = [2**i for i in range(9)]
    
    print nums
    reverseList(nums)
    print nums