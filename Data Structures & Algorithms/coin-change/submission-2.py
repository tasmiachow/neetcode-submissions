class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        memo = {}
        
        def dfsHelper(i, coins, amount):
            if amount == 0:
                return 0
            if amount <0 or i == len(coins):
                return float("inf")
            if (i,amount) in memo: 
                return memo[(i, amount)]
            #skip
            minCoins = dfsHelper(i+1, coins, amount)

            #include i 
            c = 1 + dfsHelper(i, coins, amount-coins[i])
            
            minCoins=min(minCoins, c)
            memo[(i, amount)] = minCoins
            return minCoins
        result = dfsHelper(0, coins, amount)
        return result if result != float('inf') else -1


            