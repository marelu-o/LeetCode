class Solution {
public:
    int missingNumber(vector<int>& nums) {

        // Versão NÃO Otimizada
        int soma_esperada = 0;
        for (int i = 0; i <= nums.size(); i++){
            soma_esperada += i;
        }

        int soma_real = 0;
        for(int i = 0; i < nums.size(); i ++){
            soma_real += nums[i];
        }

        return soma_esperada - soma_real;
    }
};