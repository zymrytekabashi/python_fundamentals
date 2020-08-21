class Underscore:
    def map(self, iterable, callback):
        for i in range(len(iterable)):
            iterable[i]=callback(iterable[i])
        return iterable
       
    def find(self, iterable, callback):
    # your code here
        result=[]
        for i in range(len(iterable)):
            if callback(iterable[i]) == True:
                result.append(iterable[i])
        return result
    
    def filter(self, iterable, callback):   
        result=[]
        for i in range(len(iterable)):
            if callback(iterable[i]) == True:
                result.append(iterable[i])
        return result
                
                           
                
    
    def reject(self, iterable, callback):
        result=[]
        for i in range(len(iterable)):
            if callback(iterable[i]) != True:
                result.append(iterable[i])
        return result
# you just created a library with 4 methods!
# let's create an instance of our class
_ = Underscore() # yes we are setting our instance to a variable that is an underscore
evens = _.map([1,2,3], lambda x: x*2)
evens2 = _.find([1,2,3,4,5,6], lambda x: x>4)
evens3=_.filter([1,2,3,4,5,6], lambda x: x%2==0) # should return [2,4,6]
evens4=_.reject([1,2,3,4,5,6], lambda x: x%2==0) # should return [1,3,5]



# should return [2, 4, 6] after you finish implementing the code above
_.map([1,2,3], lambda x: x*2) # should return [2,4,6]
_.find([1,2,3,4,5,6], lambda x: x>4) # should return the first value that is greater than 4
_.filter([1,2,3,4,5,6], lambda x: x%2==0) # should return [2,4,6]
_.reject([1,2,3,4,5,6], lambda x: x%2==0) # should return [1,3,5]

print(evens)
print(evens2)
print(evens3)
print(evens4)