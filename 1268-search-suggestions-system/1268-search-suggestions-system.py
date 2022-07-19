class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        res=[]
        l,r=0,len(products)-1
        for i in range(len(searchWord)):
            c=searchWord[i]
            while l<=r and (len(products[l])<=i or products[l][i]!=c):
                l += 1
            while l<=r and (len(products[r])<=i or products[r][i]!=c):
                r -= 1
            
            temp=[]
            for i in range(min(3,r-l+1)):
                temp.append(products[l+i])
            res.append(temp)
        return res
            