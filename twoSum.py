class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            c=target-nums[i]
            if c in nums and nums.index(c)!=i:
                return [nums.index(c),i]



