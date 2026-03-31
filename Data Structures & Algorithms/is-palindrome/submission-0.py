class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        word = ''
        for i in s:
            if i.isalnum():
                word += i.lower()

        r = len(word)-1

        for i in range(len(word)):

            if word[i] == word[r]:
                print(i,r)
                print(word[i], word[r])
                r-=1
            else:
                return False
            
            if r < i:
                continue

        return True