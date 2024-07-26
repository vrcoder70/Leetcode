'''
Question : Given an m x n matrix, return all elements of the matrix in spiral order.

# Intuition
The problem of traversing a matrix in spiral order involves visiting each element in a clockwise manner, starting from the top-left corner and progressively narrowing the boundaries as we move inward.

# Approach
1. Initialization: Define pointers for the left (`l`), right (`r`), top (`t`), and bottom (`d`) boundaries of the matrix. Initialize an empty list `res` to store the result.
2. Helper Functions: Create helper functions to traverse a row or a column within the current boundaries:
    - `rowHelper(row, l, r)`: Appends elements from the specified row within the left and right boundaries.
    - `colHelper(c, t, d)`: Appends elements from the specified column within the top and bottom boundaries.
3. Spiral Traversal: Use a `while` loop to repeatedly traverse the matrix in spiral order:
    - Traverse from left to right along the top boundary, then move the top boundary down.
    - Traverse from top to bottom along the right boundary, then move the right boundary left.
    - Traverse from right to left along the bottom boundary, then move the bottom boundary up.
    - Traverse from bottom to top along the left boundary, then move the left boundary right.
    - Alternate the traversal direction and update the respective boundaries accordingly.
4. Termination: The loop terminates when the left boundary exceeds the right boundary or the top boundary exceeds the bottom boundary.

# Complexity
- Time complexity: O(mn), where m is the number of rows and n is the number of columns. Each element of the matrix is visited exactly once.
- Space complexity: O(mn) for the result list that stores the elements in spiral order. No additional space is required beyond this.

'''

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Chain of Thought
        # matrix[t][l to r]
        # t += 1
        # matrix[t to d][r]
        # r -= 1
        # matrix[d][r to l]
        # d-=1
        # matrix[d to t][l]
        # l+=1
        l,r = 0,len(matrix[0])-1
        t,d = 0,len(matrix)-1
        
        res = []

        def rowHelper(row,l,r):
            step = 0
            if l <= r:
                step =1
            else:
                step =-1
            for i in range(l,r+step, step):
                res.append(matrix[row][i])
            
        
        def colHelper(c,t,d):
            step = 0
            if t <= d:
                step = 1
            else:
                step = -1
            for i in range(t,d+step, step):
                res.append(matrix[i][c])
            
        change = True
        while l<=r:
            if change:
                rowHelper(t, l, r)
                t += 1
                if t > d:
                    break
                colHelper(r, t, d)
                r -= 1
            else:
                rowHelper(d, r, l)
                d -= 1
                if t > d:
                    break
                colHelper(l, d, t)
                l += 1
            change = not change
            
        return res 
