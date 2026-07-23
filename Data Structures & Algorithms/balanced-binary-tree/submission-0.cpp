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

    int height(TreeNode* root){
        if(!root){return 0;}
        return 1+ max(height(root->left), height(root->right));
    }
    bool isBalanced(TreeNode* root) {
        
        if(!root){return true;}
        
        //get the left and right
        //check if their height difference is no more than 1

        int lt = height(root->left);
        int rt = height(root->right);
        if(lt - rt != 0 && lt-rt!= 1 && lt-rt != -1){
            return false;
        }
        // check later nodes

        return isBalanced(root->left) && isBalanced(root->right);
    }
};
