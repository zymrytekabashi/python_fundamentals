# import the python testing framework
import unittest
# our "unit"
# this is what we are running our test on
def isEven(n):
    if n % 2 == 0:
       return True
    else:
       return False
   
def reverseList(my_list):
    length = int(len(my_list)/2)
    for i in range(length):
        my_list[i],my_list[len(my_list)-1-i] = my_list[len(my_list)-1-i],my_list[i]
    return my_list

def coins(money):
    my_list=[]
    my_list.append(money//25)
    money = money%25
    my_list.append(money//10)
    money = money%10
    my_list.append(money//5)
    money = money%5
    my_list.append(money//1)
    return my_list
    
def factorial(number):
    result=1
    for i in range (1,int(number)+1):
       result = result * i
        
    return result

         
def fibonnaci(number):
    if number >=1:
               
        if number == 1:
            return 0
        elif number ==2:
            return 1
        else:
            return fibonnaci(number-1)+fibonnaci(number-2)
    else:
        return False        
    

def isPalindrome(my_word):
    length = int(len(my_word)/2)
    for i in range(length):
        if my_word[i] != my_word[len(my_word)-i-1]:
            return False
    return True
        

class IsEvenTests(unittest.TestCase):
    def testTwo(self):
        self.assertEqual(reverseList([1,3,5]), [5,3,1])
        self.assertNotEqual(reverseList([1,2,3]),[3,2,1])
        self.assertTrue(reverseList([1,2,3]))
        self.assertFalse(reverseList([1,2,3]))
    def testThree(self):
        self.assertEqual( isPalindrome("racecar"), True ) 
        self.assertTrue( isPalindrome("racecar"))
        self.assertFalse( isPalindrome("rabcr") )
        self.assertNotEqual( isPalindrome("rabcr"), True )
        
    def testFour(self):
        self.assertEqual( coins(87), [3, 1, 0, 2] ) 
        self.assertTrue( coins(87), [3, 1, 0, 2] )
        self.assertFalse( coins(95), [3, 1, 0, 2]  )
        self.assertNotEqual( coins(95), [3, 1, 0, 2] )
        self.assertIn(3, coins(87))
        
    def testFive(self):
        self.assertEqual( factorial(5), 20 ) 
        self.assertTrue( factorial(5), 20 )
        self.assertFalse( factorial(5), 30  )
        self.assertNotEqual( factorial(5), 30 )
        
    def testSix(self):
        self.assertEqual( fibonnaci(5), 3 ) 
        self.assertTrue( fibonnaci(5), 3 )
        self.assertFalse( fibonnaci(5), 30  )
        self.assertNotEqual( fibonnaci(5), 30 )
        
        
    
    def setUp(self):
        print('running setUp')
        
    def tearDown(self):
        print("running tearDown tasks")
if __name__ == '__main__':
    unittest.main() # this runs our tests
