class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if sorted(list(s)) == sorted(list(t)):
        #     return True
        # return False

        s_map = {}
        t_map = {}

        if len(s) != len(t):
            return False

        for i in s:
            if i in s_map.keys():
                s_map[i] += 1
            else:
                s_map[i] = 1

        for i in t:
            if i not in s_map:
                return False
            
            s_map[i] -= 1

            if s_map[i] < 0 :
                return False

        return True