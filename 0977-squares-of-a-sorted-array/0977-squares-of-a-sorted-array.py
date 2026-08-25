class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        
        # Versão UM pouco mais Otimizada O(n \log n)

        for i in range(len(nums)):
            nums[i] = nums[i] * nums[i]
        nums.sort()
        return nums
        '''

        # Versão Otimizada usando ponteiros O(n)
        n = len(nums)
        esquerda = 0
        direita = n - 1
        
        resultado = [0] * n 


        for i in range(n - 1, -1, -1):
            quadrado_esq = nums[esquerda] * nums[esquerda]
            quadrado_dir = nums[direita] * nums[direita]
            

            if quadrado_esq > quadrado_dir:
                resultado[i] = quadrado_esq
                esquerda += 1
            else:
                resultado[i] = quadrado_dir
                direita -= 1

        return resultado
        '''
        