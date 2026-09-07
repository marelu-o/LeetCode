class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        // LINHAS DE OTIMIZAÇÃO DE I/O
        std::ios_base::sync_with_stdio(false);
        std::cin.tie(NULL);
        
        unordered_set <int> nums_dupl;

        for(int i = 0; i < nums.size(); i++){
            int num = nums[i];

            if(nums_dupl.find(num) != nums_dupl.end()){
                return true;
            }

            nums_dupl.insert(num);
        }

        return false;
    }
};