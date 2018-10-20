def distinctList(nums):
    distinct = set()
    for i in nums:
        if i in distinct:
            return False
        distinct.add(i)
    return True

if __name__ == '__main__':
    
    print 'Distinct elements in the list :',distinctList([1,4,5,3,6,8,9,3])