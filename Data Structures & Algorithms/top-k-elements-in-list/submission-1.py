class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        result = []


        for i in nums:
            hm[i] = hm.get(i, 0) + 1

        print(hm)
        
        while len(result) < k:
            max_freq = 0
            for i,j in hm.items():
                print("elem", i)
                print("elem value", j)
                if j > max_freq:
                    max_freq = j
                    elem_added = i
                    print("max_freq elem_added",max_freq, elem_added)

            print(max_freq, i, j, elem_added)
            result.append(elem_added)
            hm.pop(elem_added)

        return result