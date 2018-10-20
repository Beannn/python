class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        d = {}
        nums.sort()
        s = set()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] in d:
                     d[nums[i] + nums[j]].append((i, j))
                else:
                    d[nums[i] + nums[j]] = [(i,j)]

        for i in range(len(nums)):
            for j in range(i + 1, len(nums) - 2):
                t = target - nums[i] - nums[j]
                if t in d:
                    for k in d[t]:
                        if k[0] > j:
                            s.add((nums[i], nums[j], nums[k[0]], nums[k[1]]))
        return [list(i) for i in s]

a =  Solution()
a.fourSum([1,0,-1,0,-2,2],0)