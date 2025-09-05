class Calculator:
    def sum(self, a, b):
        result = a + b
        return result
    def sub(self, a, b):
        result = a - b
        return result
    def mul(self, a, b):
        return a*b
    def div(self, a, b):
        if b == 0: raise ArithmeticError("На ноль не делить!")
        return a/b
    def pow(self, a, b):
        return a**b
    def avg(self, nums):
        s = 0
        for num in nums:
            if (len(nums) == 0): return 0
            s = s + num
            l = len(nums)
        return self.div(s, l)