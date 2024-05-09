class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        ans = list(s)
        start = 0
        end = len(ans) -1
        while start < end:
            if (not s[start].isalpha()) :
                start += 1
                continue
            if not s[end].isalpha():
                end -= 1
                continue
            temp = ans[start]
            ans[start] = ans[end]
            ans[end] = temp
            start += 1
            end -= 1
        return ''.join(ans)
            
print(Solution().reverseOnlyLetters("7_28]"))