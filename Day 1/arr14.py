class Solution:
    def longestCommonPrefix(self, strs: List[str]):
        if len(strs) == 0:
            return ""
            
        result = ""
        base = strs[0]
        for i in range(len(base)):
            for c in strs[1:]:
                if i == len(c) or c[i] != base[i]:
                    return result
            result += base[i]   # add after checking all words
        return result
