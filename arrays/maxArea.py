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
def calcMaxArea(arr):
    """
    """

    dist = len(arr)
    last_item = arr[-1]
    res = []

    for i in arr:
        dist -= 1
        m = min(i, last_item)
        a = dist * m
        res.append(a)
    
    return max(res)


def maxArea( A): 
    l = 0
    r = len(A) -1
    area = 0
      
    while l < r: 
        # Calculating the max area 
        area = max(area, min(A[l],  
                        A[r]) * (r - l)) 
      
        if A[l] < A[r]: 
            l += 1
        else: 
            r -= 1
    return area 
