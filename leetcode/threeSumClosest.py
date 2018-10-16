class Solution(object):
    class Solution:
        def threeSumCloset(self, nums, target):
            """
            :type nums: List[int]
            :rtype: List[List[int]]
            """
            nums.sort()
            i = 0
            minnDiff = sys.maxsize
            res = 0
            while i < len(nums) - 2:
                j = i + 1
                k = len(nums) - 1
                while j < k:
                    sum = nums[i] + nums[j] + nums[k]
                    diff = abs(sum - target)
                    if diff < minnDiff:
                        minnDiff = sum - target
                        res = sum
                    if sum > target:
                        k -= 1
                    elif sum < target:
                        j += 1
                    else:
                        return res
            return res
