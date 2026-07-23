#include<map>
class Solution {
public:
    bool isNStraightHand(vector<int>& hand, int groupSize) {
        if(hand.size() % groupSize != 0){
            return false;
        }
        sort(hand.begin(), hand.end());
        map<int, int> freq; //maps value to frequency

        for(int i = 0; i < hand.size(); ++i){
            freq[hand[i]]++;
        }
        for(auto it = freq.begin(); it != freq.end(); ++it){
            int start = it->first;
            while(it->second > 0){
                freq[it->first]--;
                for(int i = start + 1; i < start + groupSize; ++i){
                    if(freq.find(i) != freq.end() && freq.find(i)->second != 0){
                        freq[i]--;
                    }
                    else{
                        return false;
                    }
                }
            }
        }
        return true;
    }
};
