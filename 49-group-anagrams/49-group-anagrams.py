class Solution:
    def groupAnagrams(self, strs):
        dct=defaultdict(list)
        for i in strs:
            s="".join(sorted(i))
            dct[s].append(i)
        return dct.values()
        