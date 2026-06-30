class Solution {
public:
    bool canJump(vector<int>& nums) {
        // Algoritmo Guloso:
        // Verifica de trás para frente
        
        int meta = nums.size() - 1;
        for (int i = nums.size() - 1; i >= 0; i--){
               if (i + nums[i] >= meta){
                meta = i;
               }
        }
        if (meta == 0){
            return true;
        } else {
            return false;
        }
    }
};