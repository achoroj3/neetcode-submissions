using namespace std;
#include <set>


class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        set<int> intmap;
        for (int i = 0; i < nums.size(); i++){
            auto it = intmap.find(nums[i]);
            if (it == intmap.end()){
                intmap.insert(nums[i]);
            }
            else{
                return true;
            }
            
        }
        return false;
    }
};
