from typing import List
from math import floor, ceil

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        def findKthElementIn2Arrays(arr1: List[int], arr2: List[int], k) -> int:
            l1, l2 = len(arr1), len(arr2)
            if l1 < l2: l1, l2, arr1, arr2 = l2, l1, arr2, arr1
            if l2 == 0: return arr1[k - 1]
            if k == 1: return min(arr1[0], arr2[0])
            k1 = arr1[floor(k / 2) - 1]
            k2 = float('inf')
            if l2 >= floor(k / 2): k2 = arr2[floor(k / 2) - 1]
            if k1 < k2:
                return findKthElementIn2Arrays(arr1[floor(k / 2):], arr2, ceil(k / 2))
            else:
                return findKthElementIn2Arrays(arr1, arr2[floor(k / 2):], ceil(k / 2))

        l1, l2 = len(nums1), len(nums2)
        left, right = floor((l1 + l2 + 1) / 2), ceil((l1 + l2 + 1 ) / 2)
        return (findKthElementIn2Arrays(nums1, nums2, left) + findKthElementIn2Arrays(nums1, nums2, right)) / 2