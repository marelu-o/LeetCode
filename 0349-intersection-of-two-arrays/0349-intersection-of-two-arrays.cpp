class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        /*
        // O(n²)
        unordered_set<int> nums3;
        for (int i = 0; i < nums1.size(); i++) {
            // A busca (find) em um vector é linear O(n), tornando o loop O(n²)
            if (find(nums2.begin(), nums2.end(), nums1[i]) != nums2.end()) {
                nums3.insert(nums1[i]);
            }
        }
        return vector<int>(nums3.begin(), nums3.end());
        */

        // O(n): tabela hash (unordered_set em C++)
        unordered_set<int> set1(nums1.begin(), nums1.end());
        unordered_set<int> resultSet;
        
        for (int num : nums2) {
            // .count() em um unordered_set opera em tempo constante O(1)
            if (set1.count(num)) {
                resultSet.insert(num);
            }
        }
        
        return vector<int>(resultSet.begin(), resultSet.end());
    }
};