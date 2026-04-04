class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = 0
        r = len(s) - 1 

        while l < r:
            fchar = s[l]
            lchar = s[r]
            temp = fchar
            fchar = lchar
            lchar = temp
            s[l] = fchar
            s[r] = lchar
            l+=1
            r-=1

        return s 