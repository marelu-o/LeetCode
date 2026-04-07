class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
       vector<vector<int>> resultado;

       sort(nums.begin(), nums.end());
        do {
            
               resultado.push_back(nums);
            
        } while (next_permutation(nums.begin(), nums.end()));
    return resultado;
    }

};