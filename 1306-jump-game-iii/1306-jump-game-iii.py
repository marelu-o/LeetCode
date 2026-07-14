class Solution(object):
    def solve(self, arr, start, dp, n):
        # Verifica se o índice está fora dos limites
        if start >= n or start < 0:
            return False
        
        # Verifica se a posição já foi visitada
        if dp[start]:
            return False
        
        # Condição de vitória: encontrou o zero
        if arr[start] == 0:
            return True
            
        # Marca a posição atual como visitada
        dp[start] = True
        
        # Chamadas recursivas para a direita e para a esquerda
        return self.solve(arr, start + arr[start], dp, n) or \
               self.solve(arr, start - arr[start], dp, n)

    def canReach(self, arr, start):
        n = len(arr)
        # Cria uma lista de booleanos (Falso) com o tamanho do array
        dp = [False] * n 
        
        # Inicia a recursão
        return self.solve(arr, start, dp, n)
    
    
