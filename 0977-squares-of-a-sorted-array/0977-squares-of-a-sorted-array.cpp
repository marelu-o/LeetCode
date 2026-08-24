class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {

        // Versão NÃO Otimizada
        /*for(int i = 0; i < nums.size(); i++){
            nums[i] = pow(nums[i], 2);
        }
        sort(nums.begin(), nums.end()); //O(n log n)
        
        return nums;*/ 

        // Versão UM pouco mais Otimizada
        /* for(int i = 0; i < nums.size(); i++){
            nums[i] = nums[i] * nums[i];
        }
        sort(nums.begin(), nums.end()); //O(n log n)
        
        return nums;*/ 


        // Versão Otimizada usando ponteiros (O(n))
        int esquerda = 0;
        int direita = nums.size() - 1;
        vector<int> resultado(nums.size());

        for(int i = nums.size() - 1; i >= 0; i--){
            if(abs(nums[esquerda] * nums[esquerda]) > abs(nums[direita] * nums[direita])){
                resultado[i] = abs(nums[esquerda] * nums[esquerda]);
                esquerda++;
            } else {
                resultado[i] = abs(nums[direita] * nums[direita]);
                direita--;
            }
        }

        return resultado;
        
    }
};