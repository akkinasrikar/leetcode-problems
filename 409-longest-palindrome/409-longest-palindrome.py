from collections import Counter
class Solution:
    def longestPalindrome(self, s):
        c,l,f=Counter(s),0,0
        for i in c.items():
            if i[1]%2==0: l=l+i[1]
            else: f,l=1,l+i[1]-1
        return l+f