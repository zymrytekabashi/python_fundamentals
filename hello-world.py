# 1. TASK: print "Hello World"
print( 'Hello World' )

# 2. print "Hello Noelle!" with the name in a variable
name = "Zuma"
print('Hello',name ,'!' )	# with a comma
print( 'Hello '+ name  + '!')	# with a +

# 3. print "Hello 42!" with the number in a variable
num = 12
print( 'Hello', num )	# with a comma
print( 'Hello ' + str(num) )	# with a +	-- this one should give us an error!
# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "pasta"
fave_food2 = "pizza"
print( 'I love to eat {} and {}.' .format(fave_food1,fave_food2) ) # with .format()
print(f'I love to eat {fave_food1} and {fave_food2}' ) # with an f string

# Playing around with other string methods
print('Hello '+ name.upper())
print('Hello '+ name.lower())
a= name.islower()
b=name.isnumeric()
print(a)
print(b)

name2 = "Hello, Zuma."
s=name2.center(20)
x = name2.find("u", 2, 10)
y=name.isspace()
z=name2.replace('u','i')
print(x)
print(y)
print(z)
print(s)

