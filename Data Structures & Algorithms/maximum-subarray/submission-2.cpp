class Solution {
public:
    int maxSubArray(vector<int>& nums) {
       // two variables
       //one tracking current max and absolute max

        int rsum = nums[0];
        int csum = 0;
        for(int i = 0; i < nums.size(); ++i){
            //how do we make a decision!?
            //add to csum
            if (nums[i] > csum){
                if(csum > 0){
                    csum+= nums[i];
                }
                else{
                    csum = nums[i];   
                }
            }
            else{
                csum+= nums[i];
            }


            //reset to current element

            rsum = std::max(csum, rsum);

        }
        return rsum;
    }
};
