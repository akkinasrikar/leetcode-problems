class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        s=sum(salary)
        s=s-salary[0]-salary[-1]
        s=s/(len(salary)-2)
        return s
        