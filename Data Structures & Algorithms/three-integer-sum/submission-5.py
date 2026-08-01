class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        # h = {}
        # for ind in range(len(nums)):
        #     h[nums[ind]] = ind
        nums.sort()
        for i in range(len(nums)-2):
            
            lv = -nums[i]
            left = i+1
            right = len(nums) - 1
            while left < right:
                if nums[left] + nums[right] == lv:
                    triplet = tuple(sorted([nums[i], nums[left], nums[right]]))
                    res.add(triplet)
                    right -= 1
                    left +=1
                elif nums[left] + nums[right] > lv:
                    right -= 1
                else:
                    left +=1

        return [list(t) for t in res]