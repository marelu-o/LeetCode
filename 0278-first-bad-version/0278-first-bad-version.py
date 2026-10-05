# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        a = 1         
        b = n         
        while (a<=b):             
            k = (a+b)//2              
            if isBadVersion(k):                 
                r = k                 
                b = k-1             
            else:                 
                a = k+1         
        return r 