#Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = 'Brad'
age = 37

#Concatenate
print('Hello, my name is' + name + 'and i am ' + str(age))

#String formatting

#Arguments by position
print('My name is  {name} and i am {age}'.format(name=name, age=age))

#F-Strings (3.6+)
print(f'Hello, my name is {name} and i am {age}')

#String Methods

s = 'hello world'

#capitalize strings
print(s.capitalize())