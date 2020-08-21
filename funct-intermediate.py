x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# modify elemnts in list
x[1][0]=15
students[0]['last_name']='Bryant'
sports_directory['soccer'][0]='Andres'
z[0]['y']=30
print(x)
print(students[0]['last_name'])
print(sports_directory['soccer'][0])
print(z)

# 2 
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# This exercise was done based on the lecture we had yesterday so  I hope this does not violate your policy rules:|
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(my_list):
    for x in range(0, len(my_list)):
        for y in my_list[x]:
            if(y=='first_name'):
                print(y+' - '+my_list[x][y], end=',')
            else:
                print(y + ' - ' + my_list[x][y])
        
iterateDictionary(students)
        
        
# 
def iterateDictionary2(key,my_list):
    for x in my_list:
        print(x[key])
iterateDictionary2('last_name',students)

# 4

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}


def printInfo(my_list):
   
    for key in dojo:
        print(f'{len(dojo[key])} {key}')
    for location in dojo[key]:
        print(location)
        
    
        
            
        
printInfo(dojo)
print(len(dojo['locations']))


        
    
    

# python code below!
arr = [1,3,5,7]
arr[0], arr[1] = arr[1], arr[0]
print(arr)