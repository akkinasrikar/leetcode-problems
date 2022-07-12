class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res=[]
        for i in asteroids:
            while len(res) and i<0 and res[-1]>0:
                if i==-res[-1]: 
                    res.pop()
                    break
                elif res[-1]<-i:
                    res.pop()
                    continue
                elif res[-1]>-i:
                    break
            else:
                res.append(i)
        return res
        