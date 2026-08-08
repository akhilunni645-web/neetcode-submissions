from typing import List
import heapq


class Twitter:

    def __init__(self):
        # user -> set of users they follow
        self.followMap = {}

        # user -> list of (time, tweetId)
        self.tweetMap = {}

        # Global timestamp
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        # Make sure user exists
        if userId not in self.followMap:
            self.followMap[userId] = set()

        if userId not in self.tweetMap:
            self.tweetMap[userId] = []

        # Add tweet
        self.tweetMap[userId].append((self.time, tweetId))

        # Increase time
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:

        # Max heap
        # Python has a min heap, so use negative time
        heap = []

        # User should see their own tweets
        users = set()

        # Add user themselves
        users.add(userId)

        # Add everyone they follow
        if userId in self.followMap:
            users.update(self.followMap[userId])

        # Put the most recent tweet from each user
        # into the heap
        for user in users:

            if user in self.tweetMap and self.tweetMap[user]:

                index = len(self.tweetMap[user]) - 1

                time, tweetId = self.tweetMap[user][index]

                heapq.heappush(
                    heap,
                    (-time, tweetId, user, index)
                )

        result = []

        # Get at most 10 tweets
        while heap and len(result) < 10:

            negTime, tweetId, user, index = heapq.heappop(heap)

            result.append(tweetId)

            # Move to the next older tweet from this user
            index -= 1

            if index >= 0:

                time, tweetId = self.tweetMap[user][index]

                heapq.heappush(
                    heap,
                    (-time, tweetId, user, index)
                )

        return result

    def follow(self, followerId: int, followeeId: int) -> None:

        # Make sure follower exists
        if followerId not in self.followMap:
            self.followMap[followerId] = set()

        # Follow the user
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:

        # Remove follow relationship
        if followerId in self.followMap:
            self.followMap[followerId].discard(followeeId)