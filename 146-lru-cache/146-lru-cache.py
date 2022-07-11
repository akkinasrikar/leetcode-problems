class LRUCache:

    def __init__(self, capacity: int):
        self.dct=collections.OrderedDict()
        self.cap=capacity

    def get(self, key: int) -> int:
        if key not in self.dct: return -1
        v=self.dct.pop(key)
        self.dct[key]=v
        return v

    def put(self, key: int, value: int) -> None:
        if key in self.dct: self.dct.pop(key)
        else:
            if self.cap>0:
                self.cap -= 1
            else:
                self.dct.popitem(last=False)
        self.dct[key]=value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)