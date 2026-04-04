class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        # ref_word_len = 0
        lcp = ""

        # while ref_word_len < len(strs[0]):
        #     char = strs[0][ref_word_len]
        #     for i in range(1, len(strs)):
        #         if ref_word_len >= len(strs[i]) or char != strs[i][ref_word_len]:
        #             return lcp
                
        #     lcp+=char
        #     ref_word_len +=1

        # return lcp


        #interview friendly solution
        sorted_strs = sorted(strs)
        first_str = sorted_strs[0]
        last_str = sorted_strs[-1]

        for i,j in zip(first_str, last_str):
            if i!=j:
                return lcp

            lcp+=i

        return lcp

