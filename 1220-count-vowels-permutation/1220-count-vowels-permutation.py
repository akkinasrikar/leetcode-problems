class Solution:
    def countVowelPermutation(self, n: int) -> int:
        mod=10**9+7
        vowels={"a":1,"e":2,"o":2,"u":1,"i":4}
        @lru_cache(None)
        def dp(last,n):
            if n==1:
                if last==None: return 5
                else: return vowels[last]
            res=0
            if last==None:
                res += dp("a",n-1)+dp("e",n-1)+dp("i",n-1)+dp("o",n-1)+dp("u",n-1)
                res %= mod
            else:
                if last=="a": res += dp("e",n-1)
                if last=="e": res += dp("a",n-1)+dp("i",n-1)
                if last=="i": res += dp("a",n-1)+dp("e",n-1)+dp("o",n-1)+dp("u",n-1)
                if last=="o": res += dp("i",n-1)+dp("u",n-1)
                if last=="u": res += dp("a",n-1)
                res %= mod
            return res 
        return dp(None,n)