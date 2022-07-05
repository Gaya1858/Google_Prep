from typing import List


class FileSharing:

    def __init__(self, m: int):
        self.file = m
        self.userId = 1

    def join(self, ownedChunks: List[int]) -> int:
        pass


    def leave(self, userID: int) -> None:
        pass

    def request(self, userID: int, chunkID: int) -> List[int]:
        pass

# Your FileSharing object will be instantiated and called as such:
# obj = FileSharing(m)
# param_1 = obj.join(ownedChunks)
# obj.leave(userID)
# param_3 = obj.request(userID,chunkID)