class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # Pega cada combinação gerada diretamente do range e transforma em lista
        return [list(comb) for comb in itertools.combinations(range(1, n + 1), k)]
        