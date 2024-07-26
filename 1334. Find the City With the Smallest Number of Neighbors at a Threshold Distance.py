'''There are n cities numbered from 0 to n-1. Given the array edges where edges[i] = [fromi, toi, weighti] represents a bidirectional and weighted edge between cities fromi and toi, and given the integer distanceThreshold.

Return the city with the smallest number of cities that are reachable through some path and whose distance is at most distanceThreshold, If there are multiple such cities, return the city with the greatest number.

Notice that the distance of a path connecting cities i and j is equal to the sum of the edges' weights along that path.'''

from collections import defaultdict
import heapq

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        
        adject = defaultdict(list)

        for frm,to,wei in edges:
            adject[frm].append((to,wei))
            adject[to].append((frm,wei))
        
        def dijkstra(src):
            heap = [(0,src)]
            visit = set()

            while heap:
                dist, node = heapq.heappop(heap)
                if node in visit:
                    continue
                visit.add(node)
                for nei, dist2 in adject[node]:
                    threshold = dist + dist2
                    if threshold <= distanceThreshold:
                        heapq.heappush(heap, (threshold, nei))
            return len(visit)-1
        
        res,min_count = -1,n
        for src in range(n):
            count = dijkstra(src)
            if count <= min_count:
                res,min_count = src,count
        return res