'''You are given two 0-indexed strings source and target, both of length n and consisting of lowercase English letters. You are also given two 0-indexed character arrays original and changed, and an integer array cost, where cost[i] represents the cost of changing the character original[i] to the character changed[i].

You start with the string source. In one operation, you can pick a character x from the string and change it to the character y at a cost of z if there exists any index j such that cost[j] == z, original[j] == x, and changed[j] == y.

Return the minimum cost to convert the string source to the string target using any number of operations. If it is impossible to convert source to target, return -1.

Note that there may exist indices i, j such that original[j] == original[i] and changed[j] == changed[i].'''


class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        adj = defaultdict(list)
        
        for i,v in enumerate(original):
            adj[v].append((changed[i],cost[i]))
        
        costMap = {}

        def dijkshtra(src,trg):
            heap = [(0,src)]
            visit =set()

            while heap:
                cost,node = heapq.heappop(heap)
                if node == trg:
                    costMap[(src,trg)] = cost
                    return cost
                
                if node in visit:
                    continue
                
                visit.add(node)
                for nei,cst in adj[node]:
                    heapq.heappush(heap, (cst+cost, nei))
            return -1
        
        cost = 0
        for s,t in zip(source, target):
            if s != t and (s,t) not in costMap:         
                cst = dijkshtra(s,t)
                if cst == -1:
                    return -1
                cost += cst
            elif (s,t) in costMap:
                cost += costMap[(s,t)]
            
        return cost
