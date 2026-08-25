class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        resultado = []
        
        # Versão NÃO Otimizada O(n^2)
        # Para cada elemento no vetor original...

        for i in range(len(nums)):
            soma_atual = 0
            # ...fazemos um NOVO laço voltando do início (0) até a posição atual (i)
            for j in range(i + 1):
                soma_atual += nums[j]
            resultado.append(soma_atual)

        # Versão Otimizada O(n)
        '''
        soma = 0
        for num in nums:
            soma += num
            resultado.append(soma)
        '''
        return resultado