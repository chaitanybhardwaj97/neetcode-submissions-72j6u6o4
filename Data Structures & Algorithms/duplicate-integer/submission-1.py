class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        l_len = len(nums)
        s_len = len(list(set(nums)))
        if s_len < l_len:
            return True
        return False