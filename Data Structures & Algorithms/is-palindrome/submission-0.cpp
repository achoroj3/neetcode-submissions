
#include <cctype>
#include <iostream>
class Solution {
public:
    bool isPalindrome(string s) {
        string palindrome;
        for (int i = 0; i < s.length(); i++){
            if(isalpha(s[i]) || isdigit(s[i])){
                palindrome += tolower(s[i]);
            }
        }
        int start = 0;
        int end = palindrome.length() - 1;

        while (start < end){
            if (palindrome[start] != palindrome[end]){
                return false;
            }
            start++;
            end--;
        }
        return true;
    }
};
