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
    void helper(TreeNode* root, vector<int> &in_order){
        if(!root){
            return;
        }
        helper(root->left, in_order);
        in_order.push_back(root->val);
        helper(root->right, in_order);
    }
    int kthSmallest(TreeNode* root, int k) {
        vector<int> in_order;
        helper(root, in_order);
        return in_order[k - 1];
    }
};
