class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        result = []
        temp = intervals[0]

        for i in range(1, len(intervals)):

            if temp[1] >= intervals[i][0]:
                print("merge possible for", i-1, i)
                temp = [temp[0], max(temp[1], intervals[i][1])]

            else:
                result.append(temp)
                temp = intervals[i]

        result.append(temp)
        return result