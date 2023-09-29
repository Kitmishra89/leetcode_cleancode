class Solution:
    def reverseWords(self, s: str) -> str:

        ans = ""
        start = len(s)-1
        end = start

        while start >= 0:

            if start == end and s[start] == ' ':
                start -=  1
                end = start
            
            elif s[start] == ' ':
                ans += s[start+1:end+1] + " "
                start -= 1
                end = start
            else:
                start -= 1

        if start != end:
            return ans + s[start+1:end+1]
        
        n =  len(ans)

        return ans[:n-1]
            

            
             
            


