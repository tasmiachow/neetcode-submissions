import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #Undestand: tims- input adjaceny list 
        # n - amt of nodes  
        # k - starting node 
        print(times)
        
        adj = {} #dictionary 
        nodes = list(range(1,n+1))
        for i in nodes:
            adj[i] = []

        # s = src, d = dst, w = weight
        for s, d, w in times:
            adj[s].append([d, w])
        print(adj)
        shortest = {}
        minHeap = [[0, k]]
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in shortest:
                continue
            shortest[n1] = w1

            for n2, w2 in adj[n1]:
                if n2 not in shortest:
                    heapq.heappush(minHeap, [w1 + w2, n2])
        print(shortest)
        if len(list(shortest.keys())) < n:
            return -1 
        
        delay_times = list(shortest.values())

        return max(delay_times)
         

        