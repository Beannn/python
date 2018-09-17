# -*- coding: utf-8 -*-
def twoSum(self, nums, target):
    dic = {}
    for i in range(len(nums)):
        if target-nums[i] in dic:
            return  i,dic[target-nums[i]]
        else:
            dic[nums[i]] = i 


    