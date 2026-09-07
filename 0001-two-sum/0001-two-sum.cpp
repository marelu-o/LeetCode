class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {

        // LINHAS DE OTIMIZAÇÃO DE I/O
        std::ios_base::sync_with_stdio(false);
        std::cin.tie(NULL);

        
        // Chave: o número | Valor: o índice 'i' onde ele foi visto
        unordered_map<int, int> caderninho;

        // Verifica se o parceiro já está no mapa
        for (int i = 0; i < nums.size(); i++){
        int parceiro = target - nums[i];
        int num = nums[i];
            if(caderninho.find(parceiro) != caderninho.end()){
                return {caderninho[parceiro], i};
            }
        // Guarda o número atual e o seu índice
        caderninho[num] = i;

        }
        // Retorna um vetor vazio caso não encontre nenhuma combinação
        return {};

    }
};