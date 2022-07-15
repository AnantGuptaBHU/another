import math
class Solution():
    def __init__(self,n1,n2):
        self.n1=n1
        self.n2=n2
        self.ans=None
    def is_amicable(self):
        if self.n1 == 1 and self.n2 == 1:
            return False
        s1 = 1
        i = 2
        while i <= math.sqrt(self.n1):
            if self.n1 % i == 0:
                if self.n1 / i == i:
                    s1 += i
                else:
                    s1 += i
                    s1 += int(self.n1 / i)
            i += 1
        s2 = 1
        i = 2
        while i <= math.sqrt(self.n2):
            if self.n2 % i == 0:
                if self.n2 / i == i:
                    s2 += i
                else:
                    s2 += i
                    s2 += int(self.n2 / i)
            i += 1
        return True if s1 == self.n2 and s2 == self.n1 else False
ami=Solution(220,284)
print(ami.is_amicable())