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
    
    int helper(TreeNode* root){
        if(!root){
            return 0;
        }
        return 1+ max(helper(root->left), helper(root->right));
    }
    int diameterOfBinaryTree(TreeNode* root) {
        if(!root){
            return 0;
        }
        int diameter = helper(root->left) + helper(root->right);
        diameter = max(diameter, diameterOfBinaryTree(root->right));
        diameter = max(diameter, diameterOfBinaryTree(root->left));
        return diameter;

    }
};
