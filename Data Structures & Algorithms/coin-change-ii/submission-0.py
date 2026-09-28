class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}

        def dfs(i, amount):
            if amount == 0:
                return 1
            elif amount < 0 or i >=len(coins):
                return 0
            if (i,amount) in memo:
                return memo[(i,amount)]
            
            #skip i 
            res = dfs(i+1, amount)
           
            #include i 
            res += dfs(i, amount - coins[i])
            memo[(i, amount)] = res
            return res
        return dfs(0, amount)
            