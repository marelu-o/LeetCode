class Solution {
public:
    vector<vector<int>> combine(int n, int k) {
        vector<vector<int>> resultado;
        vector<int> vetor;
        vector<bool> mascara(n, false);
        fill(mascara.end() - k, mascara.end(), true);
        for (int i = 1; i < n +1; i++){
           vetor.push_back(i);
        }
        vector<int> combAtual(k);

        do {
            int indice = 0;
            for(int i = 0; i< n; i++){
               if (mascara[i]){
               combAtual[indice]= vetor[i];
               indice ++;
               }
              
            }
            resultado.push_back(combAtual);
        } while (next_permutation(mascara.begin(), mascara.end()));
         return resultado;
    }
};