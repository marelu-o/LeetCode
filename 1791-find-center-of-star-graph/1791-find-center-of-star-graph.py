class Solution:
    def findCenter(self, edges: list[list[int]]) -> int:
        centro = 0
        u, v = edges[0]

        # Se o valor em edges[0] está em edges[1], logo o valor encontrado é o centro do grafo!
        if u in edges[1]:
            centro = u
        
        else: centro = v

        return centro

        