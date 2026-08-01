class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        res = []
        for i in range(len(nums)):
            h[nums[i]] = i
        print(h)
        
        for i in range(len(nums)):
            lookup_val = target - nums[i]
            print(nums[i])
            print(lookup_val)
            print(h.get(lookup_val), i)
            print('---------')
            if lookup_val in h and i != h.get(lookup_val):
                res.append(i)
                res.append(h.get(lookup_val))
                print(res)
                break

        return res