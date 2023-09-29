class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        lps = [0]*len(needle)
        prevlps, i = 0, 1   # prev prefix-suffix

        while i < len(needle):
            if needle[prevlps] ==  needle[i]:
                lps[i] = prevlps+1
                prevlps += 1
                i += 1
            elif prevlps == 0:
                lps[i] = 0
                i += 1
            else:
                prevlps = lps[prevlps-1]
        
        i , j = 0, 0

        while i < len(haystack):
            if needle[j] == haystack[i]:
                i += 1
                j += 1
            else:
                if j == 0:
                    i += 1
                else:
                    j = lps[j-1]
                    
            if j == len(needle):
                return i-j

        return -1


        
        