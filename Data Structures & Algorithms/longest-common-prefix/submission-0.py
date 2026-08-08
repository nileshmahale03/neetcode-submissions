class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort() 
        #print(strs)

        iterator = min(len(strs[0]), len(strs[-1])) #3
        #print(iterator)
        
        i = 0
        while i < iterator:
            if strs[0][i] == strs[-1][i]:
                i += 1
            else:
                break

        return strs[0][:i]
            