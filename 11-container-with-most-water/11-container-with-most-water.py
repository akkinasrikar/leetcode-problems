class Solution:
    def maxArea(self, height):
        area,l,r=0,0,len(height)-1
        while l<r:
            area=max(area,(r-l)*min(height[l],height[r]))
            if height[l]<height[r]: l += 1
            else: r -= 1
        return area