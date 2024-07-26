'''Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.'''

class Solution:
    def numTrees(self, n: int) -> int:
        
        # DP array to store the number of unique BSTs for each count of nodes
        dp = [0] * (n + 1)
        
        # Base cases
        dp[0] = 1
        dp[1] = 1
        
        # Fill the DP array
        for nodes in range(2, n + 1):
            for root in range(1, nodes + 1):
                left_trees = dp[root - 1]
                right_trees = dp[nodes - root]
                dp[nodes] += left_trees * right_trees
        
        return dp[n]
