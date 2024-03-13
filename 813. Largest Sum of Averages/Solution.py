class Solution:
    def largestSumOfAverages(self, nums: List[int], m: int) -> float:
        length = len(nums)
        prefix_sum = [0] * (length+1)
        for i in range(1, len(prefix_sum)):
            prefix_sum[i] = nums[i-1] + prefix_sum[i-1]

        f = [[0] * (m+1) for _ in range(length+1)]

        for i in range(1,length+1):
            for j in range(1,m + 1):
                if j == 1:
                    f[i][j] = prefix_sum[i] / i
                else:
                    for k in range(2,i+1):
                        f[i][j] = max(f[i][j], f[k-1][j-1] + (prefix_sum[i]-prefix_sum[k-1]) / (i-k+1))

        return f[length][m]
