class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {
        vector<int> resultado;
        int soma = 0;
        for (int i = 0; i < nums.size(); i++){
            soma += nums[i];
            resultado.push_back(soma);
        }

        return resultado;

    }
};