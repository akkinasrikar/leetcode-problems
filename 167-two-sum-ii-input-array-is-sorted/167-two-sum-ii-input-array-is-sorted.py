class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # concept : Two Pointer
        # Time : O(n) Space: O(1)
        # uncomment to get all possibilities
        
        #res=[]
        l,r=0,len(numbers)-1
        while l<r:
            temp=numbers[l]+numbers[r]
            if temp==target:
                return [l+1,r+1]
                #res.append([l+1,r+1])
                #l,r = l+1,r-1
                #while l<r and numbers[l]==numbers[l-1]: l += 1
                #while l<r and numbers[r]==numbers[r+1]: r -= 1
            elif temp<target: l += 1
            else: r -= 1
        #return res[0]
        