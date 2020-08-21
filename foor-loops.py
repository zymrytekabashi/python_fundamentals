# Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
# Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]

def biggie_size(my_list):
    new_list=[]
    str='biggie'
    for x in my_list:
        if x>0:
            new_list.append(str)
        else:
            new_list.append(x)
            
    return new_list
print(biggie_size([-1,3,5,-5]))

# Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
# Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
# Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it

def count_positives(my_list):
    count=0
    for x in my_list:
        if x>0:
            count+=1
        my_list[len(my_list)-1]=count
    return my_list
print(count_positives([-1,1,1,1]))

# Sum Total - Create a function that takes a list and returns the sum of all the values in the array.
# Example: sum_total([1,2,3,4]) should return 10
# Example: sum_total([6,3,-2]) should return 7

def sum_total(my_list):
    sum=0
    for x in my_list:
        sum=sum+x
    return sum
print(sum_total([1,2,3,4]))

# Average - Create a function that takes a list and returns the average of all the values.
# Example: average([1,2,3,4]) should return 2.5

def average(my_list):
    sum=0
    for x in my_list:
        sum+=x
    avg=sum/len(my_list)
    return avg
print(average([1,2,3,4]))

# Length - Create a function that takes a list and returns the length of the list.
# Example: length([37,2,1,-9]) should return 4
# Example: length([]) should return 0

def length(my_list):
    if len(my_list)==0:
        return 0
    else:
        return len(my_list)
    
print(length([1,2,7,8]))

# Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
# Example: minimum([37,2,1,-9]) should return -9
# Example: minimum([]) should return False

def minimum(my_list):
    min=my_list[0]
    for x in my_list:
        if len(my_list)<=0:
            return False
        else:
            if x<min:
                min=x
    return min
print(minimum([3,9,-1,-5]))

# Maximum - Create a function that takes a list and returns the maximum value in the array. If the list is empty, have the function return False.
# Example: maximum([37,2,1,-9]) should return 37
# Example: maximum([]) should return False

def maximum(my_list):
    max=my_list[0]
    for x in my_list:
        if len(my_list)<=0:
            return False
        else:
            if x>max:
                max=x
    return max
print(maximum([3,9,-1,-5]))

# Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
# Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }


def ultimate_analysis(my_list):
    sumTotal=0
    my_dict={'sumTotal', 'average','minimum','maximum'}
    min=my_list[0]
    max=my_list[0]
    for x in my_list:
        sumTotal+=x
        if x<min:
            min=x
        elif x>max:
            max=x
                
        sumTotal+=x
        avg=sumTotal/len(my_list)
        if 'sumTotal' in my_dict:
            my_dict['sumTotal']=sumTotal
        elif 'average' in my_dict:
            my_dict['average']=avg
        elif 'minimum' in my_dict:
            my_dict['minimum']=min
        elif 'maximum' in my_dict:
            my_dict['maximum']=max
    return my_dict
    
    print(ultimate_analysis([2,3,4,1]))
    
# Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
# Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]

def reverse_list(my_list):
    var=len(my_list)-1
    new_list=[]
    for x in range(var,-1, -1):
        new_list.append(my_list[x])
    return new_list
print(reverse_list([2,1,4,9]))