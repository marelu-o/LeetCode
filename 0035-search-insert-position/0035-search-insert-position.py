class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        a = 0         
        b = len(nums) - 1          
        while a <= b:             
            k = (a + b) // 2              
            if nums[k] == target:                 
                return k             
            elif nums[k] < target:                 
                a = k + 1               
            else:                 
                b = k - 1            
        return a 