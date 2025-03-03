#!/usr/bin/env python3


class Solution:
    def findMedianSortedArrays(self, nums1: list[int], 
                               nums2: list[int]) -> float:        
        joined_list = sorted(nums1 + nums2)
        n = len(joined_list)
        if n % 2 == 0:
            return (joined_list[n//2 - 1] + joined_list[n//2]) / 2.0
        else:
            return joined_list[n//2]
