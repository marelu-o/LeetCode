# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        fila = deque ([(p, q)])

        while fila: 
            no1, no2 = fila.popleft()

            if not no1 and not no2:
                continue
            
            if not no1 or not no2 or no1.val != no2.val:
                return False
            
            fila.append((no1.left, no2.left))
            fila.append((no1.right, no2.right))
        
        return True