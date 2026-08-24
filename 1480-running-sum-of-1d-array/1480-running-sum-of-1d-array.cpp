class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {
        vector<int> resultado;
        //Versão NÃO Otimizada
        // Para cada elemento no vetor original...
       /* for (int i = 0; i < nums.size(); i++) {
            int soma_atual = 0;
            
            // ...fazemos um NOVO laço voltando do início (0) até a posição atual (i)
            for (int j = 0; j <= i; j++) { 
                soma_atual += nums[j];
            }
            
            resultado.push_back(soma_atual);
        } */

        // Versão Otimizada
        int soma = 0;
        for (int i = 0; i < nums.size(); i++){
            soma += nums[i];
            resultado.push_back(soma);
        }

        return resultado;

    }
};