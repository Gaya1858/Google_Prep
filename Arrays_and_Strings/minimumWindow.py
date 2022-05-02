from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s == t:
            return t
        if len(t) > len(s):
            return ""
        td = Counter(t)

        newList = []
        for ind, val in enumerate(s):
            if val in td:
                newList.append((val, ind))

        subSeen = float("inf"), None, None
        formed = l = r = 0
        req = len(td)
        temp = {}
        while r < len(newList):
            charc = newList[r][1]
            temp[charc] = temp.get(charc, 0) + 1

            if temp[charc] == td[charc]:
                formed += 1
            while l <= r and formed == req:
                charc = newList[l][1]
                end = newList[r][0]
                start = newList[l][0]
                if end - start + 1 < subSeen[0]:
                    subSeen = (end - start + 1, start, end)
                temp[charc] -= 1
                if temp[charc] < td[charc]:
                    formed -= 1
                l += 1
            r += 1

        return "" if subSeen[0] == float("inf") else s[subSeen[1]: subSeen[2] + 1]




s = Solution()
print(s.minWindow(s = "ADOBECODEBANC", t = "ABC"))