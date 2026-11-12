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
    bool isSymmetric(TreeNode* root) {
        std::deque<std::pair<TreeNode*, TreeNode*>> fila;
        fila.push_back({root->left, root->right});
        
        while (!fila.empty()) {
            auto [esquerda, direita] = fila.front();
            fila.pop_front();
            
            if (!esquerda && !direita) {
                continue;
            }
            
            if (!esquerda || !direita || esquerda->val != direita->val) {
                return false;
            }
            
            fila.push_back({esquerda->left, direita->right});
            fila.push_back({esquerda->right, direita->left});
        }
        return true;
    }
};
