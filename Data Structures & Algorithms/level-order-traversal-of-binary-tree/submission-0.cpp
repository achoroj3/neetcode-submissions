#include <queue>

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
    vector<vector<int>> levelOrder(TreeNode* root) {
        //make the queue to perform level order
        //while there are still elements in the quee
        //make each index a representation of that level
        
        vector<vector<int>> solution;
        if(!root) return solution;
        queue<TreeNode*> q;
        
        q.push(root);
        int index = 0;
        while(!q.empty()){
            int levelsize = q.size();
            solution.push_back({});
            for(int i = 0; i < levelsize; ++i){
                TreeNode* node = q.front();
                q.pop();
                if(node){
                    q.push(node->left);
                    q.push(node->right);
                    solution[index].push_back(node->val);
                }
            }
            index++;
        }
        solution.pop_back();
        return solution;
    }
};
