'''Question : Given the root of a binary search tree and the lowest and highest boundaries as low and high, 
trim the tree so that all its elements lies in [low, high]. Trimming the tree should not change the relative structure of the elements that will remain in the tree 
(i.e., any node's descendant should remain a descendant). It can be proven that there is a unique answer.

Return the root of the trimmed binary search tree. Note that the root may change depending on the given bounds.'''

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        
        def dfs(node):
            if not node:
                return False
            while node and node.val < low:
                if node.right:
                    left,right = node.right.left,node.right.right
                    node.val = node.right.val
                    node.left = left
                    node.right = right
                else:
                    return True

            while node and node.val > high:
                if node.left:
                    left,right = node.left.left,node.left.right
                    node.val = node.left.val
                    node.left = left
                    node.right = right
                else:
                    return True

            if node and (node.val < low or node.val > high):
                n = dfs(node)
                node = None if n else node
            
            if node:
                left = dfs(node.left)
                if left:
                    node.left = None
                right = dfs(node.right)
                if right:
                    node.right = None
    
            return False
            
           
        r = dfs(root) 

        return root if not r else None