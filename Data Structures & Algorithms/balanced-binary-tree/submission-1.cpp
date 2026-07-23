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
#include<utility>
class Solution {
public:

    pair<bool, int> isBalancedhelper(TreeNode*root){
        if(!root){
            return {true, 0};
        }
        int lt = isBalancedhelper(root->left).second;
        int rt = isBalancedhelper(root->right).second;

        if(lt -rt != 0 && lt-rt != 1 && lt-rt != -1){
            return {false, 1 + max(lt, rt)};
        }

        return {(isBalancedhelper(root->left).first && isBalancedhelper(root->right).first), 1+ max(lt,rt)};
        
    }
    bool isBalanced(TreeNode* root) {
        return isBalancedhelper(root).first;
    }
};
