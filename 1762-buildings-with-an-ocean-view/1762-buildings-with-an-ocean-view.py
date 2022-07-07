class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        
        res=[]
        index=len(heights)-1
        MAX=0
        while heights:
            p=heights.pop()
            if p>MAX: 
                res.append(index)
                index -= 1
                MAX=p
            else: index -= 1
        return res[::-1]
        