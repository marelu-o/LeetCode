class Solution(object):
    def jump(self, nums):
        resultado = 0
        esquerda = direita = 0

        while direita < len(nums) - 1:
            mais_longe = 0
            for i in range (esquerda, direita + 1):
                mais_longe = max(mais_longe, i + nums[i])
            esquerda = direita + 1
            direita = mais_longe
            resultado += 1
        return resultado
        