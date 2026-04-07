import itertools # Biblioteca nativa obrigatória para usar o 'permutations'

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        resultado = []

        # O itertools entrega cada combinação no formato de tupla. Ex: (1, 2, 3)
        for permutacao in itertools.permutations(nums):
            # Precisamos converter a 'permutacao' (tupla) em uma lista padrão [1, 2, 3] 
            resultado.append(list(permutacao))

        return resultado