class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = collections.deque()
        # store the index of each number
        left, right = 0, 0 # init the boundary of the window

        while right < len(nums):
            while q and nums[q[-1]] < nums[right]:
                # while the right most of the queue smaller than the current number
                # remove that
                # the q only store the decreading order number
                q.pop()
            
            q.append(right)
            # always store each index

            if left > q[0]:
                # update the window, pop the left most index
                q.popleft()

            if right >= k-1:
                # when the window exist, append the left most value
                # which is the largest one in current window
                res.append(nums[q[0]])
                left += 1 # only update the left boundary when the window exist
            right += 1
        return res
