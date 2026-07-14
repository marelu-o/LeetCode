class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        q = deque() # Cria um deque (fila duplamente encadeada) para guardar os índices estrategicamente
        n = len(nums) # Captura o tamanho total do array
        dp = [0] * n # Cria um array 'dp' preenchido com zeros, com o mesmo tamanho de 'nums', para guardar as somas máximas
        
        dp[n-1] = nums[n-1] # Define o caso base: se você já está na última casa, a pontuação é o próprio valor da casa
        q.append(n-1) # Adiciona o último índice à fila
        
        for i in range(n-2, -1, -1): # Percorre o array de trás para frente (começa do penúltimo e vai diminuindo até 0)
            if q[0] - i > k: # Se a janela entre a posição atual 'i' e o melhor destino 'q[0]' ficou maior que o pulo permitido 'k'
                q.popleft() # Remove o índice da frente (q[0]) da fila, pois ele ficou inalcançável a partir de 'i'
                
            dp[i] = nums[i] + dp[q[0]] # A pontuação na casa 'i' é o valor dessa casa + a melhor pontuação possível disponível na frente da fila
            
            while q and dp[q[-1]] < dp[i]: # Enquanto a fila tiver elementos E a pontuação do último elemento da fila for pior que a nova pontuação 'dp[i]'
                q.pop() # Remove os elementos "fracos" do final da fila para manter a fila sempre em ordem decrescente de pontuação
                
            q.append(i) # Insere o índice atual na fila, já que ele agora é um "degrau" possível para os saltos das próximas iterações
            
        return dp[0] # Ao terminar de percorrer todo o array até o início, o resultado máximo estará no índice 0