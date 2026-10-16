class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        # Se houver apenas 1 pessoa e nenhuma relação de confiança, ele próprio é o juiz
        if n == 1:
            return 1
            
        # Vetores para contar o grau de entrada e saída de cada pessoa (tamanho n + 1)
        confia_em_alguem = [0] * (n + 1)
        recebe_confianca = [0] * (n + 1)
        
        for a, b in trust:
            confia_em_alguem[a] += 1  # 'a' confia em alguém
            recebe_confianca[b] += 1  # 'b' recebeu um voto de confiança
            
        # Procura quem atende às condições do juiz:
        #   1° Todos confiam nele;
        #   2° Ele não confia em alguém.
        
        for i in range(1, n + 1):
            if confia_em_alguem[i] == 0 and recebe_confianca[i] == n - 1:
                return i
                
        return -1