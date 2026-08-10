class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join([(str(len(string)) + '#' + string) for string in strs])
    def decode(self, s: str) -> List[str]:
        ptr = 0
        return_list = []
        print(s)
        while ptr < len(s):
            len_str = ""
            while(s[ptr]!= '#'):
                len_str += s[ptr]
                ptr+=1
            len_int = int(len_str)
            print(len_int)
            ptr+= 1
            string = s[ptr:ptr+len_int]
            return_list.append(string)
            ptr+= len_int
            
        return return_list

