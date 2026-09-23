class Solution {
public:
    bool lemonadeChange(vector<int>& bills) {

        int cinco = 0;
        int dez = 0;
        bool possivel = true;

        // Percorre as notas presentes no vetor bills
        for (int nota : bills) {
            // Caso nota == 5, acrescentamos mais uma nota ao caixa
            if (nota == 5) {
                cinco++;
            }
            // Caso nota == 10, acrescentamos mais uma nota no caixa e retiramos uma nota de 5
            else if (nota == 10) {
                if (cinco > 0) {
                    cinco--;
                    dez++;
                } else {
                    possivel = false;
                    break;
                }
            }

            // Caso nota == 20, acrescentamos mais uma nota ao caixa e retiramos uma de 10 e outra de 5 OU três de 5
            else if (nota == 20) {
                if (dez > 0 && cinco > 0) {
                    dez--;
                    cinco--;
                } else if (cinco >= 3) {
                    cinco -= 3;
                } else {
                    possivel = false;
                    break;
                }
            }
        }

        // Imprime o resultado no terminal
       return possivel;
    }
};