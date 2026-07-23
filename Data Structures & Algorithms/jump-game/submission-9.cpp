class Solution {
public:
    bool canJump(vector<int>& nums) {
        if(nums.size() == 1){
            return true;
        }
        int index = 0;
        int distance = nums[0];
        while(distance > 0){
            distance--;
            index++;
            if((index < nums.size() && nums[index] > distance) || distance == 0){
                distance = nums[index];
            }
            if(index == nums.size() - 1){
                return true;
            }
        }
        return false;
    }
};
