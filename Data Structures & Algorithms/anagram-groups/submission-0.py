class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_string_map = {}

        for s in strs:
            string  = ''.join(sorted(s))

            char_count = {}
            hash_string = ""
            for c in string:
                char_count[c] = char_count.get(c, 0) + 1
            
            for key in char_count.keys():
                hash_string += key + str(char_count[key])
            
            if hash_string in hash_string_map:
                hash_string_map[hash_string].append(s)
            else:
                hash_string_map[hash_string] = [s]

        res = []
        for value in hash_string_map.values():
            res.append(value)

        return res
