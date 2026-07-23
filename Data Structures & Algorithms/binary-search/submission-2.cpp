class Solution {
public:
    int search(vector<int>& nums, int target) {
        int low = 0;
        int high = nums.size() -1;
        int mid = (low + high) /2;

        while (low <= high){
            mid = (low + high)/2;
            if(nums[mid] == target){
                return mid;
            }
            //target is on right
            if(nums[mid] < target){
                low = mid + 1;
                
            } 
            if(nums[mid] > target){
                high = mid - 1;
            }
        }
        return -1;
    }
};
