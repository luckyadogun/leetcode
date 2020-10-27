"""
    Author: Lucky Adogun (zen_coder)
    License: MIT
    Date: 26-10-2020

    PROBLEM: Given two sorted arrays `nums1` and `nums2` of size m and n respectively,
    Return the median of the two sorted arrays.

    Example:

    nums1 = [1,2]
    nums2 = [3,4]

    return the median => (2 + 3) / 2 = 2.5
"""

def is_array_even(arr):
    return len(arr) % 2 == 0


def findMedianSortedArray(nums1, nums2):
    """
    
    Algorithm:
        0. merge both arrays
        1. sort the array
        2. find the middle of the array.
        3. if array length is even, add the item to the left to the median. Odd? return the array middle item as is. 


    """
    nums = nums1 + nums2
    nums = sorted(nums)

    middle = len(nums) // 2
    
    if is_array_even(nums):
        return sum((nums[middle], nums[middle - 1])) / 2
    else:
        return float(nums[middle])

        