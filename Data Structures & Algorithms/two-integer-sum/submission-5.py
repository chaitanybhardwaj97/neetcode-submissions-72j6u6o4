class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}

        for index, value in enumerate(nums):
            h[value] = index

        for index, value in enumerate(nums):
            complement = target - value

            if complement in h and h[complement] != index:
                return [index, h[complement]]