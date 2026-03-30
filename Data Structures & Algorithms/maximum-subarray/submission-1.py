class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        curr_sum = 0

        if len(nums) == 1:
            return nums[0]

        for i in range(len(nums)):
            curr_sum=0
            for j in range(i, len(nums)):
                    # print(nums[i:j+1])
                    curr_sum += nums[j]
                    if curr_sum > max_sum:
                        max_sum = curr_sum
            
        return max_sum
