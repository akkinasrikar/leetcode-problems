class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boats=0
        l,r=0,len(people)-1
        people.sort()
        while l<=r:
            if people[l]+people[r]<=limit:
                l += 1
            boats += 1
            r -= 1
        return boats
            