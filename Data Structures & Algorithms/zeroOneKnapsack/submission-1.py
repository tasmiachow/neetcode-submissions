class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        cache = {}
        def dfs(i, amount, cache):

            if i == len(weight) or amount < 0:
                return 0
            if (i, amount) in cache:
                return cache[(i, amount)]
            #skip 
            maxProfit = dfs(i+1, amount, cache)
            cache[(i, amount)] = maxProfit 

            if amount - weight[i] >=0: 
                include = profit[i] + dfs(i+1, amount - weight[i], cache)
                cache[(i, amount)] = max(include, maxProfit)
            return cache[(i, amount)]
        return dfs(0, capacity, cache) 