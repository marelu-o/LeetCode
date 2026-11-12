/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    bool isSameTree(TreeNode* p, TreeNode* q) {
        std::deque<std::pair<TreeNode*, TreeNode*>> fila;
        fila.push_back({p, q});
        
        while (!fila.empty()) {
            auto [no1, no2] = fila.front();
            fila.pop_front();
            
            if (!no1 && !no2) {
                continue;
            }
            
            if (!no1 || !no2 || no1->val != no2->val) {
                return false;
            }
            
            fila.push_back({no1->left, no2->left});
            fila.push_back({no1->right, no2->right});
        }
        return true;
    }
};