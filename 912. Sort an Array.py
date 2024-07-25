'''Given an array of integers nums, sort the array in ascending order and return it.

You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.
'''

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr, l, m, r):
            left = arr[l:m+1]
            right = arr[m+1:r+1]
            i,j,k = l,0,0
            while j < len(left) and k <len(right):
                if left[j] <= right[k]:
                    arr[i] = left[j]
                    j+=1
                else:
                    arr[i] = right[k]
                    k+=1
                i+=1

            while j < len(left):
                arr[i] = left[j]
                i+=1
                j+=1
            
            while k < len(right):
                arr[i] = right[k]
                i+=1
                k+=1
            
        
        def divide(arr, l,r):
            if l == r:
                return arr
            m = (l+r)//2
            divide(arr, l, m)
            divide(arr, m+1, r)
            merge(arr, l, m, r)
            return arr
        
        return divide(nums, 0, len(nums)-1)