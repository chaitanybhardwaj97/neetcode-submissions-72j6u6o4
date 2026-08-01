class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        h = {}
        for ind in range(len(nums)):
            h[nums[ind]] = ind
        
        for i in range(0,len(nums)-2):
            for j in range(i+1, len(nums)-1):
                lv = -(nums[i] + nums[j])
                if lv in h and j < h.get(lv):
                    triplet = tuple(sorted([nums[i], nums[j], lv]))
                    res.add(triplet)

        return [list(t) for t in res]