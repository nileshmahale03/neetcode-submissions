class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        nums_dict = {}

        for i, n in enumerate(nums):
            reciprocal = target - n
            if reciprocal in nums_dict:
                return [nums_dict[reciprocal], i]
            else:
                nums_dict[n] = i