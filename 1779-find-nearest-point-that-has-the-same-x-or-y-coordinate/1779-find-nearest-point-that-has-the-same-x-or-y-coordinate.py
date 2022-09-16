class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int: 
        def mhd(a,b,c,d):
            return abs(a-c)+abs(b-d)
        res=99999
        d=99999
        for idx,p in enumerate(points):
            if p[0]==x or p[1]==y:
                temp=mhd(x,y,p[0],p[1])
                if temp==d:
                    d=temp
                    res=min(res,idx)
                elif temp<d:
                    d=temp
                    res=idx
        return res if res!=99999 else -1
                
        