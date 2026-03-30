class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # if len(set(nums)) < len(nums):
        #     return True
        # return False

        # sorted_list = sorted(nums)

        # for i in range(len(sorted_list)-1):
        #     if sorted_list[i] == sorted_list[i+1]:
        #         return True
        # return False

        seen = set()
        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        
        return False