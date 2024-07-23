'''Given an array of integers nums, sort the array in increasing order based on the frequency of the values.
If multiple values have the same frequency, sort them in decreasing order.

Return the sorted array.'''
from collections import Counter

class Solution:
    def frequencySort(self, nums):
        # freq = Counter(nums)
        # freqMap = defaultdict(list)

        # for key,val in freq.items():
        #     freqMap[val].append(key)
        # freqMap = sorted(freqMap.items(), key=lambda item: item[0] )
    
        # res = []
        # for key,val in freqMap:
        #     val = sorted(val, reverse=True)
        #     for v in val:
        #         res.extend([v]*key)
        # return res

        freq_count = Counter(nums)
        
        sorted_freq_count = sorted(freq_count.items(), key=lambda x: (x[1],-x[0]))
        nums = []
        for i in range(len(sorted_freq_count)):
            val, freq = sorted_freq_count[i]
            for i in range(freq):
                nums.append(val)

        return nums