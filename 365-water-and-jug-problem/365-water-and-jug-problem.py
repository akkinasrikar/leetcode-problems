class Solution:
    def canMeasureWater(self,x,y,z):
        if x+y<z: return False
        visited=set()
        visited.add(0)
        q=deque()
        q.append(0)
        directions = [x,y,-x,-y]
        while len(q)!=0:
            curr=q.popleft()
            if curr==z: return True
            for i in directions:
                total = curr + i
                if total==z: return True
                if total<0 or total>(x+y): continue
                if total not in visited: 
                    visited.add(total)
                    q.append(total)
        return False
                
        
        