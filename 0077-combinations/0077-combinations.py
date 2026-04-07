class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        resultado = []
        vetor = list(range(1, n+1))

        for combinacao in itertools.combinations(vetor, k):
            resultado.append(list(combinacao))

        return resultado
        