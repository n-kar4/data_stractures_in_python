import math

class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp=[-1]*(amount+1)
        return Solution.minCoins(self,coins,amount,dp)

    def minCoins(self, coins: list[int], n: int, dp: list[int]):      
        if n==0:
            return 0;        
        ans=math.inf
        for c in coins:            
            if (n-c) >= 0:
                subAns=0
                if dp[n-c] !=-1:
                    subAns=dp[n-c]+1
                else:
                    subAns=Solution.minCoins(self,coins,n-c,dp)
                if subAns!=math.inf and subAns+1 < ans :
                    ans = subAns + 1
        dp[n] = ans
        return dp[n]

print(Solution.coinChange(0,[1,2,5],191))

