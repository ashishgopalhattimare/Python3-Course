# https://www.codewars.com/kata/binary-search-tree-validation/train/python

class T:
    def __init__(self,value,left=None,right=None):
        self.value=value
        self.left=left
        self.right=right

def inorder(node, nums):
    if node == None:
        return
    
    inorder(node.left, nums)
    nums.append(node.value)
    inorder(node.right, nums)

def is_bst(node):
    #your code here
    
    validTree = True
    
    nums = []
    inorder(node, nums)
    
    length = len(nums)
    
    if length < 3:
        return True
    
    if nums[0] > nums[1]: # descending order
        for x in range(1, length):
            if nums[x-1] <= nums[x]:
                return False
                
    else: # ascending order
        for x in range(1, length):
            if nums[x-1] >= nums[x]:
                return False
    
    return True