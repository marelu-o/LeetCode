class Solution(object):
    def canJump(self, nums):
        meta = len (nums) - 1

        for i in range (len(nums) - 1, - 1, -1):
            if i + nums[i] >= meta:
                meta = i
        if meta == 0:
            return True
        else:
            return False
        