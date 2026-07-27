class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i,j in enumerate(nums):
            h[j] = i
        
        print(h)

        for i,j in enumerate(nums):
            c = target - j

            if c in nums and h[c] != i:
                return [i, h[c]]