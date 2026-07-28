class Twitter:

    def __init__(self):
        self.following = {}
        self.posts = {}
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId in self.posts:
            self.posts[userId].append([self.time, tweetId])
        else:
            self.posts[userId] = [[self.time, tweetId]]
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId in self.following:
            self.following[userId].add(userId)
        else:
            self.following[userId] = {userId}
        heap = []
        for followee in self.following[userId]:
            if followee in self.posts:
                for post in self.posts[followee]:
                    heapq.heappush(heap, post)
        result = []
        while heap and len(result) < 10:
            post = heapq.heappop(heap)
            result.append(post[1])
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following:
            self.following[followerId].add(followeeId)
        else:
            self.following[followerId] = {followeeId}

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following and followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)