class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        p2 = 0
        
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[p2] = nums[i]
                p2 = p2+1

        for i in range(p2, len(nums)):
            nums[i] = 0

        
        
        