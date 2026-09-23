class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:

        # Uso de dicionário, onde a chave inicia com o valor igual à zero.
        caixa = {5: 0, 10: 0}

        # Percorre as notas presentes no vetor bills
        for nota in bills:

            # Verifica se a nota recebida já está em nosso caixa
            # Caso nota == 5, acrescentamos mais uma nota ao caixa
            if nota == 5:
                caixa[5] += 1

            # Caso nota == 10, acrescentamos mais uma nota no caixa e retiramos uma nota de 5
            elif nota == 10:
                if caixa[5] > 0:
                    caixa[5] -= 1
                    caixa[10] += 1
                else:
                    return False

            # Caso nota == 20, acrescentamos mais uma nota ao nosso caixa e retiramos um nota de 10 e outra de 5 OU retiramos três notas de 5
            elif nota == 20:
                if caixa[10] > 0 and caixa[5] > 0:
                    caixa[10] -= 1
                    caixa[5] -= 1
                elif caixa[5] >= 3:
                    caixa[5] -= 3
                else:
                    return False

        return True   