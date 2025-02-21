class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        prefixStr = strs[0]

        for i in range(1, len(strs)):
            n = min(len(prefixStr), len(strs[i]))

            sign = 1
            for j in range(n):
                if prefixStr[j] != strs[i][j]:
                    sign = -1
                    prefixStr = prefixStr[:j]
                    break

            prefixStr = prefixStr[:n]

            if not prefixStr:
                return ""
            
        return prefixStr