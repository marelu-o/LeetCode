class Solution {
public:
    int missingNumber(vector<int>& nums) {

        // Versão NÃO Otimizada (O (n))
       /* int soma_esperada = 0;
        for (int i = 0; i <= nums.size(); i++){
            soma_esperada += i;
        }

        int soma_real = 0;
        for(int i = 0; i < nums.size(); i ++){
            soma_real += nums[i];
        }

        return soma_esperada - soma_real;*/

        //Versão NÃO Otimizada com Sort (O(n log n))
        /*sort(nums.begin(), nums.end());

        for (int j = 0; j < nums.size(); j++){
            if(j != nums[j]){
                return j;
            }
        }
       return nums.size();*/

       // Versão Otimizada (O(n))
       // Fórmula de Gauss:

       int soma_esperada = (nums.size() * (nums.size() + 1)) / 2;
       int soma_real = 0;
        for (int i = 0; i < nums.size(); i++) {
            soma_real += nums[i];
        }
        
        return soma_esperada - soma_real;

    }
};