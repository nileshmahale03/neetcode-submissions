class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        my_dict = {}

        for i in range(n):
            compliment = target - nums[i]
            #print(compliment)
            if compliment in my_dict:
                return [my_dict[compliment], i]
            else:
                my_dict[nums[i]] = i
            #print(my_dict)
