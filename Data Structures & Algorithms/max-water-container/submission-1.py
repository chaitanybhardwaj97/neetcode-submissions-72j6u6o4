        
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        maxArea = 0

        while l<r:
        	area = min(heights[l],heights[r]) * (r-l)
        	print(area)
        	if heights[l] > heights[r]:
        		r-=1
        	else:
        		l+=1
        	if area > maxArea:
        		maxArea = area

        return maxArea