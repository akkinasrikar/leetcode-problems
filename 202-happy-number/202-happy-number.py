class Solution:
    def isHappy(self, n: int) -> bool:
        hashmap = set()
        while n!=1:
            n=sum([int(i)**2 for i in str(n)])
            if n in hashmap: return False
            else: hashmap.add(n)
        return True
        