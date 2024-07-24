'''You are given a 0-indexed integer array mapping which represents the mapping rule of a shuffled decimal system. mapping[i] = j means digit i should be mapped to digit j in this system.

The mapped value of an integer is the new integer obtained by replacing each occurrence of digit i in the integer with mapping[i] for all 0 <= i <= 9.

You are also given another integer array nums. Return the array nums sorted in non-decreasing order based on the mapped values of its elements.

Certainly! Here is the detailed explanation and example run-through for the provided code:

### Intuition
The problem requires sorting an array of numbers based on their mapped values. Each digit in a number is mapped to another digit according to the provided `mapping` array. Our goal is to transform each number based on this mapping, sort the numbers according to these transformed values, and return the sorted numbers in their original form but sorted by their mapped values.

### Approach
1. **Mapping Digits**: For each number in the input array, transform it by replacing each digit according to the given mapping.
2. **Store Mapped Values**: Store both the transformed (mapped) value and the original number in a list of tuples.
3. **Sort**: Sort the list of tuples based on the mapped values.
4. **Return Sorted Numbers**: Extract and return the original numbers from the sorted list of tuples.

### Example Run-Through
Given the input:
- `mapping = [8,9,4,0,2,1,3,5,7,6]`
- `nums = [991, 338, 38]`

Steps to solve:

1. **Mapping Process**:
    - For `991`:
        - `9` maps to `6`
        - `9` maps to `6`
        - `1` maps to `9`
        - Mapped value is `669`
    - For `338`:
        - `3` maps to `0`
        - `3` maps to `0`
        - `8` maps to `7`
        - Mapped value is `007` or `7` after removing leading zeros
    - For `38`:
        - `3` maps to `0`
        - `8` maps to `7`
        - Mapped value is `07` or `7` after removing leading zeros

2. **Form Tuples**:
    - `991` -> `(669, 991)`
    - `338` -> `(7, 338)`
    - `38` -> `(7, 38)`

3. **Sort Tuples**:
    - Sorted tuples based on the first element of the tuple (mapped value): `[(7, 338), (7, 38), (669, 991)]`

4. **Extract Original Numbers**:
    - Extract the second element from each tuple in sorted order: `[338, 38, 991]`

Final Output:
- `[338, 38, 991]`

### Complexity
- **Time Complexity**: 
  - Mapping digits takes \(O(d)\) for each number, where \(d\) is the number of digits.
  - Sorting the list of tuples takes \(O(n \log n)\), where \(n\) is the length of the `nums` array.
  - Overall, the time complexity is \(O(n \cdot d + n \log n)\).

- **Space Complexity**: 
  - Storing the list of tuples requires \(O(n)\) additional space.
  - Overall, the space complexity is \(O(n)\).

### Summary
The code effectively sorts the numbers based on their mapped values by transforming each digit according to the given mapping, sorting the transformed numbers, and returning the original numbers in sorted order. This ensures that the original relative order is maintained for numbers with the same mapped value.

'''


def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            original = num
            temp = []
            while num != 0:
                val = mapping[num % 10]
                temp.append(val)
                num = num // 10
            
            if original == num:
                temp.append(mapping[original])
            
            mappedVal = 0
            for val in reversed(temp):
                mappedVal = (mappedVal * 10) + val
            res.append((mappedVal, original))
        
        res = sorted(res, key=lambda x: x[0])
        return [ val for mappedVal,val in res ]