#include <map>
class Solution {
public:
    bool isAnagram(string s, string t) {
        map<char, int> smap;
        map<char,int> tmap;
        if (s.length() != t.length())
          return false;
        for (int i = 0; i < s.length(); ++i){
          smap[s[i]]++;
        }
        for (int i = 0; i < t.length(); ++i){
          tmap[t[i]]++;
        }
        for (auto it = smap.begin(); it != smap.end(); ++it){
            if (it->second != tmap[it->first]){
                return false;
            }
        }
        return true;
        
    }
};
