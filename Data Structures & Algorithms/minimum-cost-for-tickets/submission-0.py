class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        '''find all combinations of passes so 
            1 day pass for every single day. 
            then check if '''
        dp = {}

        def dfs(i: int) -> int:
            if i == len(days):
                return 0
            if i in dp:
                return dp[i]

            # Option 1: 1-day pass
            res = costs[0] + dfs(i + 1)

            # Option 2: 7-day pass
            j = i
            while j < len(days) and days[j] < days[i] + 7:
                j += 1
            res = min(res, costs[1] + dfs(j))

            # Option 3: 30-day pass
            j = i
            while j < len(days) and days[j] < days[i] + 30:
                j += 1
            res = min(res, costs[2] + dfs(j))

            dp[i] = res
            return res

        return dfs(0)