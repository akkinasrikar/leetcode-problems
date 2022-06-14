class MyQueue:

    def __init__(self):
        
        self.c=[]

    def push(self, x: int) -> None:
        self.c.append(x)

    def pop(self) -> int:
        return self.c.pop(0)

    def peek(self) -> int:
        return self.c[0]

    def empty(self) -> bool:
        return len(self.c)==0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()