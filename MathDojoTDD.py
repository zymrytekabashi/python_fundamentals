
import unittest


def add(self, num, *nums):
    result=num
    for i in nums:
        result += i
    return result 
            
def subtract(self, num, *nums):
    result = num
    for i in nums:
        result -= i
    return self       



class MathDojo(unittest.TestCase):
    
    def testOne(self):
        self.assertEqual( add(2,3,4), 9 )         
        
    def setUp(self):
        print('running setUp')
        
    def tearDown(self):
        print("running tearDown tasks")
if __name__ == '__main__':
    unittest.main() # this runs our tests
