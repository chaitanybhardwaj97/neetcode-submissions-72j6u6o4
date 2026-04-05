class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict

        mp = defaultdict(list)

        for word in strs:
            key = ''.join(sorted(word))
            mp[key].append(word)

        return list(mp.values())
