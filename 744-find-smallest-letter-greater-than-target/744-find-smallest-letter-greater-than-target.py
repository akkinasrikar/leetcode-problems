class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        ln=len(letters)
        L,T=letters,target
        l,h=0,ln-1
        if target<L[0] or target>=L[h]: return L[l]
        while l<=h:
            m=(l+h)//2
            M=L[m]
            if T<M: h=m-1
            else: l=m+1
        return L[l]