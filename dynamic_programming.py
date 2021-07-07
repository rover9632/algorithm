import random


def knapsack(profits, weights, capacity):
    if len(profits) == 0 or capacity <= 0 or len(profits) != len(weights):
        return 0
    
    dp = [0] * (capacity + 1)
    for c in range(capacity + 1):
        if weights[0] <= c:
            dp[c] = weights[0]
    
    for i in range(len(weights)):
        for c in range(capacity, 0, -1):
            profit1 = dp[c]
            profit2 = 0
            if c - weights[i] >= 0:
                profit2 = profits[i] + dp[c - weights[i]]
            dp[c] = max(profit1, profit2)
    
    return dp[capacity]


def can_partition(nums):
    sum_ = sum(nums)
    if len(nums) == 0 or sum_ % 2 != 0:
        return False
    
    dp = [False] * (sum_ // 2 + 1)
    dp[0] = True

    for i in range(len(nums)):
        for s in range(sum_ // 2, 0, -1):
            if dp[s] or (s >= nums[i] and dp[s - nums[i]]):
                dp[s] = True

    return dp[sum_ // 2]


def max_sub_sum(a):
    max_ = float("-inf")
    pos = None
    for leng in range(1, len(a) + 1):
        for i in range(len(a) + 1 - leng):
            sum_ = sum(a[i: i+leng])
            if sum_ > max_:
                max_ = sum_
                pos = (i, i + leng)
    return max_, pos


def max_sub_sum_dp(a):
    dp = a[:]
    for i in range(1, len(a)):
        if dp[i - 1] > 0:
            dp[i] = dp[i - 1] + a[i]
        # dp[i] = max(dp[i - 1] + a[i], a[i])
    return max(dp)


def main(args):
    '''
    # a = [1, 2, 3, 4, 5, 5]
    a = [2, 3, 4, 6, 7, 44]
    print(can_partition(a))
    '''

    '''
    r = knapsack([1, 6, 10, 16],  [1, 2, 3, 5], 6)
    print(r)
    '''

    a = list(range(-50, 50))
    a = random.choices(a, k=10)
    print(a)
    print(max_sub_sum(a))
    print(max_sub_sum_dp(a))
