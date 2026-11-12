# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []
            
        fila = deque([root])
        resposta = []

        while fila:
            tamanho_fila = len(fila)
            nivel_atual = []
            for i in range(tamanho_fila):
                no = fila.popleft()
                nivel_atual.append(no.val)
                if no.left:
                    fila.append(no.left)
                if no.right:
                    fila.append(no.right)
            
            resposta.append(nivel_atual)

        return resposta


