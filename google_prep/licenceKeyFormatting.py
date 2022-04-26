# You are given a license key represented as a string s that consists of only alphanumeric characters and dashes. The string is separated into n + 1 groups by n dashes. You are also given an integer k.
#
# We want to reformat the string s such that each group contains exactly k characters, except for the first group, which could be shorter than k but still must contain at least one character. Furthermore, there must be a dash inserted between two groups, and you should convert all lowercase letters to uppercase.
#
# Return the reformatted license key.

class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s_new = s.split('-')
        temp1 = "".join([x for x in s_new ])
        new_str = ""
        if len(temp1) == 0:
            return ""
        elif len(temp1) < k:
            return s
        elif len(temp1) % k == 0:
            for i in range(0, len(temp1),k):
                new_str = new_str + temp1[i: i+k]+"-"
        else:
            for i in range(len(temp1)-1, -1, -k):
                if i >= k:
                    new_str = "-"+ temp1[i-k+1:i+1] + new_str
                else:
                    i+=1
                    break

            if 0 < i < k:
                new_str = temp1[0: i] + new_str

        if new_str[0] == '-':
            return new_str[1:len(new_str)].upper()
        elif new_str[len(new_str)-1] == '-':
            return new_str[0:len(new_str)-1].upper()

        else:
            return new_str.upper()


sel =  Solution()
#s = "5F3Z-2e-9-w"
#k = 4
#s = "2-4A0r7-4k"

s = "---"
k = 3
sel.licenseKeyFormatting(s,k)
