class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        q = deque() 
        n = len(nums)
        dp = [0] * n 
        
        dp[n-1] = nums[n-1] 
        q.append(n-1)
        
        # Estratégia que olha de trás para frente
        for i in range(n-2, -1, -1): 
            # Se o pulo for maior que o limite(k) tira o indice de 'q'
            if q[0] - i > k: 
                # retira o primeiro elemento da fila
                q.popleft() 
            
            # dp[i] recebe o somatório do maior valor da fila com o valor atual de nums[i]            
            dp[i] = nums[i] + dp[q[0]]
            
            # Enquanto a fila não estiver vazia e o menor valor analisado for menor que o valor atual somado
            while q and dp[q[-1]] < dp[i]: 
                # retira o último elemento da fila
                q.pop() 

            # adiciona à fila o índice atual    
            q.append(i) 
            
        return dp[0] 