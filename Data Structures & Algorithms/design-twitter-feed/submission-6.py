class Twitter:
    def __init__(self):
        self.tweets = defaultdict(list)
        self.followees = defaultdict(set) 
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        allTweets = []

        for time, tweet in self.tweets[userId][-10:]:
            allTweets.append((-time, tweet))

        for followee in self.followees[userId]:
            for time, tweet in self.tweets[followee][-10:]:
                allTweets.append((-time, tweet))

        heapq.heapify(allTweets)        
        l = len(allTweets)

        for i in range(min(l,10)):
            time, tweet = heapq.heappop(allTweets)
            res.append(tweet)
        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followees[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId and followeeId in self.followees[followerId]:
            self.followees[followerId].remove(followeeId)
