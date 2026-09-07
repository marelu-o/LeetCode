class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
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