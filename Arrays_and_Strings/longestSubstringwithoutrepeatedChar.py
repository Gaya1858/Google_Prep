# Given a string s, find the length of the longest substring without repeating characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        str_1 = ""
        res = 0
        for i in range(len(s)):
            if s[i] not in str_1:
                str_1 +=  s[i]

            else:
                res = max(res, len(str_1))
                if i < len(s)-1:
                    count = 0
                    for j in str_1[::-1]:
                        if s[i] != j:
                            count += 1
                        else:
                            break
                    str_1 = str_1[len(str_1) -(count): len(str_1)] +s[i]



                else:
                    str_1 = ""

        return max(res, len(str_1))

s =Solution()
print(s.lengthOfLongestSubstring("ohvhjdml"))