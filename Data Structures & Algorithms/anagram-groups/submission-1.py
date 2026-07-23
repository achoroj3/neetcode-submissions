class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # ["act", "cat"]
        # how tf do i tell theyre anagrams
        #what if i convert the words into a frequency table. 
        #if the frequencies match, they are anagrams, and their
        #indexes should be grouped together. 
        adict = dict()
        alphabet = dict()
        for i in range(26):
            alphabet[i] = chr(97 + i)
        for index, string in enumerate(strs):
            temp_key = [0] * 26
            for c in string:
                temp_key[ord(c) - ord('a')]+= 1
            key = ""
            for char_index, elem in enumerate(temp_key):
                key += alphabet[char_index] * elem
            if key not in adict.keys():
                adict[key] = []
            print(key)
            adict[key].append(index)
        grouped = [[]]
        for values in adict.values():
            sublist = []
            for elem in values:
                sublist.append(strs[elem])
            grouped.append(sublist)
        return grouped[1:]
