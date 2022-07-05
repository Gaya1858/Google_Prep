from collections import defaultdict
from typing import List
import heapq


class Twitter:

    def __init__(self):

        self.tweetDict = defaultdict(list)
        self.followDict = defaultdict(set)
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetDict[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []
        self.followDict[userId].add(userId)
        for followeeId in self.followDict[userId]:
            if followeeId in self.tweetDict:
                index = len(self.tweetDict[followeeId]) - 1
                count, tweetId = self.tweetDict[followeeId][index]
                minHeap.append([count, tweetId, followeeId, index - 1])
        heapq.heapify(minHeap)
        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweetDict[followeeId][index]
                heapq.heappush(minHeap,[count, tweetId, followeeId, index - 1])

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followDict[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followDict[followerId]:
            self.followDict[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
s = Twitter()
s.postTweet(1, 5)
print(s.getNewsFeed(1))
s.follow(1, 2)
s.postTweet(2, 6)
print(s.getNewsFeed(1))
# s.unfollow(1, 2)
print(s.getNewsFeed(1))
s.follow(2, 3)
s.postTweet(3, 7)
print(s.getNewsFeed(2))