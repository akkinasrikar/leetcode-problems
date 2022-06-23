class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.dct={}
        value=0
        for i in wordsDict:
            if i in self.dct: self.dct[i].append(value)
            else: self.dct[i]=[value]
            value += 1        
        #print(self.dct)
    def shortest(self, word1: str, word2: str) -> int:
        a=self.dct[word1]
        b=self.dct[word2]
        res=999999
        for i in a:
            for j in b: res=min(res,abs(i-j))
        return res

# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)