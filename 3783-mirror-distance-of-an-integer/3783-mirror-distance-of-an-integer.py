class Solution:
    def mirrorDistance(self, n: int) -> int:
        caractere = str(n)
        inverso = int(caractere[:: -1])
        return abs(n - inverso)