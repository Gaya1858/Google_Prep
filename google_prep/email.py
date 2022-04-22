# Every valid email consists of a local name and a domain name, separated by the '@' sign. Besides lowercase letters, the email may contain one or more '.' or '+'.
#
# For example, in "alice@leetcode.com", "alice" is the local name, and "leetcode.com" is the domain name.
# If you add periods '.' between some characters in the local name part of an email address, mail sent there will be forwarded to the same address without dots in the local name. Note that this rule does not apply to domain names.
#
# For example, "alice.z@leetcode.com" and "alicez@leetcode.com" forward to the same email address.
# If you add a plus '+' in the local name, everything after the first plus sign will be ignored. This allows certain emails to be filtered. Note that this rule does not apply to domain names.
#
# For example, "m.y+name@email.com" will be forwarded to "my@email.com".
# It is possible to use both of these rules at the same time.
#
# Given an array of strings emails where we send one email to each emails[i], return the number of different addresses that actually receive mails.
from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        # split emails first as two parts, one is upto '@' but not '@'
        # second one is after '@'
        split_email = [x.split('@') for x in emails]
        email = set()
        # loop through spli_email to join the username and check for any '+'
        for i in split_email:
            em = ""
            for j in i[0]:
                if j == '+':
                    break
                elif j != '.':
                    em += "".join(j)
            em += '@'
            em +="".join(i[1])
            email.add(em)
        return len(email)


sel = Solution()
emails = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]
print(sel.numUniqueEmails(emails))