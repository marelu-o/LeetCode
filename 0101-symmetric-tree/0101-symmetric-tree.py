# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        fila = deque ([(root.left, root.right)])

        while fila:
            esquerda, direita = fila.popleft()

            if not esquerda and not direita:
                continue
            
            if not esquerda or not direita or esquerda.val != direita.val:
                return False
            
            fila.append((esquerda.left, direita.right))
            fila.append((esquerda.right, direita.left))
        
        return True