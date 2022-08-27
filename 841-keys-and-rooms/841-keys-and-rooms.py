class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        s=set()
        s.add(0)
        def dfs(n):
            if n in s: return
            else:
                s.add(n)
                for i in rooms[n]: dfs(i)
        for i in rooms[0]: dfs(i)
        return [False,True][len(s)==len(rooms)]
            