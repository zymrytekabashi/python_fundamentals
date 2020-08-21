


class MathDojo:
    def __init__(self):
    	self.result = 0
    def add(self, num, *nums):
        self.result+=num
        for i in nums:
            self.result += i
        
        return self
            
    def subtract(self, num, *nums):
        self.result -= num
        for i in nums:
            self.result -= i
        return self
   
     
# create an instance:
md = MathDojo()
# to test:
# y=md.add(2,3,4).result
# a=md.add(2,1,2,3).result
# b=md.add(6,7,1).result
# y=md.substract(2,3,4).result
# a=md.substract(2,1,2,3).result
# b=md.substract(6,7,1).result

x = md.add(2).add(2,5,1).subtract(3,2).result
# y = md.add(5).add(2,3,2).subtract(5,1,2).result

# y=md.add(2,3,4).result
# print(y)
# print(a)
# print(b)
print(x)	# should print 5
# print(y)
# run each of the methods a few more times and check the result!
