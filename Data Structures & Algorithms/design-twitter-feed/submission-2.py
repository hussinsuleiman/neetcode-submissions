class Twitter:
    def __init__(self):
        self.tweets = defaultdict(list)
        self.followees = defaultdict(set) 
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((tweetId, self.time))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        allTweets = []
        allTweets.append(self.tweets[userId].copy())

        for followee in self.followees[userId]:
            allTweets.append(self.tweets[followee].copy())
        
        l = len(allTweets)

        for i in range(10):
            idMax = 0

            for i in range(1, l):
                if not allTweets[idMax]:
                    idMax = i
                elif allTweets[i] and allTweets[i][-1][1] > allTweets[idMax][-1][1]:
                    idMax = i
            
            if allTweets[idMax]:
                res.append(allTweets[idMax][-1][0])
                allTweets[idMax].pop()
        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followees[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId and followeeId in self.followees[followerId]:
            self.followees[followerId].remove(followeeId)
