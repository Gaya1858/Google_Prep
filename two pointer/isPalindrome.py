import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        m = re.split('[^a-zA-Z0-9]+', s)
        string = ''.join(i for i in m).lower( )
        if string[::-1] == string:
            return True
        return False
s=Solution()
print(s.isPalindrome("0p"))