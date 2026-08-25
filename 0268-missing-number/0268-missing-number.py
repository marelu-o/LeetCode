class Solution:
    def missingNumber(self, nums: list[int]) -> int:

        # Versão NÃO Otimizada 1 (Fazendo a soma manualmente com For)
        # Complexidade de Tempo: O(n)
        '''
        soma_esperada = 0
        # range vai de 0 até o tamanho de nums (inclusivo)
        for i in range(len(nums) + 1):
            soma_esperada += i
            
        soma_real = 0
        # range vai de 0 até o tamanho de nums - 1
        for i in range(len(nums)):
            soma_real += nums[i]
            
        return soma_esperada - soma_real
        '''

        # Versão NÃO Otimizada 2 (Usando Ordenação / Sort)
        # Complexidade de Tempo: O(n log n)
        '''
        nums.sort()

        for j in range(len(nums)):
            if j != nums[j]:
                return j
                
        return len(nums) # Retorna o tamanho caso o faltante seja o último
        '''

        # Versão Otimizada (Fórmula de Gauss + Sum)
        # Complexidade de Tempo: O(n)
        n = len(nums)
        soma_esperada = (n * (n + 1)) // 2 
        soma_real = sum(nums) 
        
        return soma_esperada - soma_real
        