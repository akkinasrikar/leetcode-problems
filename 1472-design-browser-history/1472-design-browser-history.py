class Node:
    def __init__(self,val,Prev=None,Next=None):
        self.val=val
        self.Prev=Prev
        self.Next=Next
class BrowserHistory:

    def __init__(self, homepage: str):
        self.curr=Node(homepage)

    def visit(self, url: str) -> None:
        new=Node(url)
        new.Prev=self.curr
        self.curr.Next=new
        self.curr=new

    def back(self, steps: int) -> str:
        while steps!=0 and self.curr.Prev:
            self.curr=self.curr.Prev
            steps -= 1
        return self.curr.val

    def forward(self, steps: int) -> str:
        while steps!=0 and self.curr.Next:
            self.curr=self.curr.Next
            steps -= 1
        return self.curr.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)