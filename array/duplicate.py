#!/usr/bin/env python3


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''
        Class that handles duplicates
        '''
        k = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1

        return k
