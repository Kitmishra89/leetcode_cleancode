class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_len = 0
        stack_char = list()
        stack_index = list()
        stack_index.append(-1)

        for i, char in enumerate(s):
            if char == '(':
                stack_char.append(char)
                stack_index.append(i)
                
            else:
                if stack_char and stack_char[-1] == '(':
                    stack_char.pop()
                    stack_index.pop()
                    max_len = max(max_len, i-stack_index[-1])

                else:
                    stack_index.append(i)

        return max_len









        
        