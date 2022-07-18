import numpy as np
class Solution(object):
    def kClosest(self, points, k):
        res=[]
        for p in points:
            res.append([p,self.distance(p)])
        res=sorted(res,key=lambda x:x[1])
        return [res[i][0] for i in range(k)]
    def distance(self,point):
        return np.sqrt(point[0]**2+point[1]**2)
    
        