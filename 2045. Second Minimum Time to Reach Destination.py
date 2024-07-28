'''
A city is represented as a bi-directional connected graph with n vertices where each vertex is labeled from 1 to n (inclusive). The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself. The time taken to traverse any edge is time minutes.

Each vertex has a traffic signal which changes its color from green to red and vice versa every change minutes. All signals change at the same time. You can enter a vertex at any time, but can leave a vertex only when the signal is green. You cannot wait at a vertex if the signal is green.

The second minimum value is defined as the smallest value strictly larger than the minimum value.

For example the second minimum value of [2, 3, 4] is 3, and the second minimum value of [2, 2, 4] is 4.
Given n, edges, time, and change, return the second minimum time it will take to go from vertex 1 to vertex n.

Notes:

You can go through any vertex any number of times, including 1 and n.
You can assume that when the journey starts, all signals have just turned green.'''

class Solution:

    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:

        g = [[] for _ in range(n + 1)]

        for u, v in edges:

            g[u].append(v)

            g[v].append(u)

        

        q = deque([(1, 1)])

        shortest = [-1] * (n + 1)

        second_shortest = [-1] * (n + 1)

        shortest[1] = 0

        while q:

            x, freq = q.popleft()

            t = shortest[x] if freq == 1 else second_shortest[x]

            if (t // change) % 2:

                t = change * (t // change + 1) + time

            else:

                t += time

            for y in g[x]:

                if shortest[y] == -1:

                    shortest[y] = t

                    q.append((y, 1))

                elif second_shortest[y] == -1 and shortest[y] != t:

                    if y == n:

                        return t

                    second_shortest[y] = t

                    q.append((y, 2))

        return 0

        