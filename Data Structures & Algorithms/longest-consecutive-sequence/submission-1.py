class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setnums = set(nums)
        long_seq = -99999
        start_seq = -999999
        nums_start = []

        if len(nums) < 1:
            return 0
            
        for i in nums:
            if i - 1 not in setnums:
                nums_start.append(i)

        for i in nums_start:
            count = 1
            while i + 1 in setnums:
                i+=1
                count+=1

            if count > long_seq:
                long_seq = count

        return long_seq 