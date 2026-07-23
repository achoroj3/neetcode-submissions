#include <algorithm>
class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int actual = nums[0];
        int expected = 0;
        for(int i = 1; i < nums.size(); ++i){
            actual += nums[i];
            expected+= i;
        }
        expected += nums.size();
        return expected - actual;

    }
};
