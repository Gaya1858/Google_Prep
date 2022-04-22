# You are given a license key represented as a string s that consists of only alphanumeric characters and dashes. The string is separated into n + 1 groups by n dashes. You are also given an integer k.
#
# We want to reformat the string s such that each group contains exactly k characters, except for the first group, which could be shorter than k but still must contain at least one character. Furthermore, there must be a dash inserted between two groups, and you should convert all lowercase letters to uppercase.
#
# Return the reformatted license key.

class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:

        temp = "".join([x for x in s.split('-')])
        str_ttl = len(temp)
        print(temp, str_ttl)
        count = k
        new_str = ""
        if str_ttl % k == 0:
            for i in range(len(temp),k):
                new_str = new_str +"-"
        if new_str[len(new_str)-1] == '-':
            return new_str[0:len(new_str)-1].upper()


        return new_str.upper()


sel =  Solution()
# s = "5F3Z-2e-9-w"
# k = 4
s = "2-5g-3-J"
k = 2
sel.licenseKeyFormatting(s,k)
