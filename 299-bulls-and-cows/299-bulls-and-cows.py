from collections import Counter
class Solution(object):
    def getHint(self, secret, guess):
        s, g = Counter(secret), Counter(guess)
        a = sum(i == j for i, j in zip(secret, guess))
        res='%sA%sB' % (a, sum((s & g).values()) - a)
        return res
        