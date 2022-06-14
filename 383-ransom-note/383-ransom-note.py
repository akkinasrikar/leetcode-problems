class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for i in ransomNote:
            if i in magazine:
                idx = magazine.index(i)
                magazine = magazine[:idx]+magazine[idx+1:]
            else: return False
        return True
        