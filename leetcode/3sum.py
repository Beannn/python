class Solution:
    def twosum(self,nums, target):
        dic = {}
        ll = []
        t = []
        if nums is None:
            return ll
        for i in range(len(nums)):
            if target - nums[i] in dic:
                if (nums[dic[target - nums[i]]], nums[i]) not in t:
                    ll.append([nums[dic[target - nums[i]]], nums[i]])
                    t.append((nums[dic[target - nums[i]]], nums[i]))
            else:
                dic[nums[i]] = i
        return ll


    def threeSum(self,nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        超时
        """
        t = []
        res = []
        if isinstance(nums, list):
            nums.sort()
            for i in range(0, len(nums)):
                ts = -nums[i]
                l = self.twosum(nums[i+1:], ts)
                for ll in l:
                    if ([nums[i]]+ll) not in t:
                        t.append(([nums[i]]+ll))
                        res.append([nums[i]]+ll)
        return res


class Solution(object):
    class Solution:
        def threeSum(self, nums):
            """
            :type nums: List[int]
            :rtype: List[List[int]]
            """
            tmp = dict()
            for i in range(len(nums)):
                tmp[nums[i]] = tmp.get(nums[i], 0) + 1
            left = sorted(filter(lambda x: x < 0, tmp))
            right = sorted(filter(lambda x: x >= 0, tmp))
            if 0 in tmp and tmp[0] > 2:
                res = [[0, 0, 0]]
            else:
                res = []
            for i in left:
                for j in right:
                    mid = -i - j
                    if mid in tmp:
                        if mid in (i, j) and tmp[mid] > 1:
                            res.append([i, mid, j])
                        elif mid < i or mid > j:
                            res.append([i, mid, j])
            return res

class Solution:
    def threeSum(self,nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res= []
        i = 0
        while i < len(nums) - 2:
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    res.append([nums[i],nums[j] , nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    j += 1
            i += 1
            while i < len(nums) - 2 and nums[i] == nums[i-1]:
                i += 1
        return res
