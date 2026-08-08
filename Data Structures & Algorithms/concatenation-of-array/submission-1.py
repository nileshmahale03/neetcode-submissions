class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = []

        for j in range(2):
            for i in range(n):
                output.append(nums[i])

        return output
        