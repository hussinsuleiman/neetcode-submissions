class Twitter:
    def __init__(self):
        self.tweets = defaultdict(list)
        self.followees = defaultdict(set) 
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((-self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        allTweets = []
        
        if self.tweets[userId]:
            allTweets.append((self.tweets[userId][-1][0], self.tweets[userId][-1][1], userId, -2))

        L = dict() 
        L[userId] = len(self.tweets[userId])

        for followee in self.followees[userId]:
            if self.tweets[followee]:
                allTweets.append((self.tweets[followee][-1][0], self.tweets[followee][-1][1], followee, -2))
                L[followee] = len(self.tweets[followee])

        heapq.heapify(allTweets)        

        for i in range(10):
            if not allTweets:
                break

            time, tweet, followee, pointer = heapq.heappop(allTweets)
            res.append(tweet)
            
            if -L[followee] <= pointer:
                heapq.heappush(allTweets, (self.tweets[followee][pointer][0], self.tweets[followee][pointer][1], followee, pointer-1))
        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followees[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId and followeeId in self.followees[followerId]:
            self.followees[followerId].remove(followeeId)
