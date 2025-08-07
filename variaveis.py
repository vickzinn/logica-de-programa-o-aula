# comment: this is my first comment in this code, but it is a test
"""
this is my first block lines in python
"""
print("hello world, this is my first code in python")
print("this is my second line of code")

"""
you use # to comment a single line (fast comment)
you use 3 quotation marks --> aspas to comment a block of lines 
"""
print(20*"a","\nconcatenatin text\n",20*"b")
# comment: you use \n to break the line

name = "vitinho"
print(name)
'''
i can create a veriable using the = sign
and in example i use the name variable that i created
'''
age = 16
year_of_birth = 2008

"""
primeiro exercicio: concatena minha idade, nome e data de nascimento
my first exercise:concatenate my age, name and year of birth
"""

print("my name is", name, "and my age is", age, "years old," " because i was born in", year_of_birth)

#type of variables
print(30*"-", 'types', 30*"-")
name
age
year_of_birth
active = True
height = 1.80

print("the type of the variable name is:", type(name))
print("the type of the variable age is:", type(age))
print("the type of the variable year is:", type(year_of_birth))
print("the type of the variable active is:", type(active))
print("the type of the variable height is:", type(height))

# comment: operators
print(30*"-", 'operators', 30*"-")

num1 = 10
num2 = 6
f1 = 2


plus = num1+num2 
division = num1/num2 #simple division
whole_division = num1//num2 #whole division 
multiplication = num1*num2
subtraction = num1-num2 
rest = num1%num2 #rest of division
rest_1 = num1%f1
rest_2 = num2%f1

print('the result of sum is:', plus)
print('the result of division is:', division)
print('the result of whole division is:', whole_division)
print('the result of multiplication is:', multiplication)
print('the result of subtraction is:', subtraction)
print('the result of percentage is:', rest)
print('the result of rest of num1 is:', rest_1)
print('the result of rest of num2 is:', rest_2)

print(30*"-", 'operators of comparation', 30*"-")
#comparation operators

num1 > num2
num1 < num2
num1 >= num2
num1 <= num2
num1 == num2
num1 != num2

print('the result of comparation is:', num1 > num2) 
print('the result of comparation is:', num1 < num2) 
print('the result of comparation is:', num1 >= num2)
print('the result of comparation is:', num1 <= num2)
print('the result of comparation is:', num1 == num2)
print('the result of comparation is:', num1 != num2)

print(90*"-")

current_year = 2025
current_year += 1
current_year -= 1

print("the current year is:", current_year) # comment: you can use += to add a value to the variable
print("the passed year is:", current_year - 1) # comment: you can use -= to subtract a value from the variable
print("the next year is:", current_year + 1) # comment: you can use += to add a value to the variable
print('my age is:', current_year - year_of_birth)
print('my age in next year is:', current_year - year_of_birth + 1)
print('my age in last year was:', current_year - year_of_birth - 1)

'''
logical operators
and, or, not
'''
print(30*"-", 'data entry', 30*"-")
#input - recive a value from user
input_name = input('what is your name?')
print('welcome to python sistem', input_name)

print(30*"-", 'calculator', 30*"-")
 
number1 = input('put the first number:')
number2 = input('put the second number:')

plus_1 = int(number1) + int(number2)
division_1 = int(number1) / int(number2) 
whole_division_1 = int(number1) // int(number2)
multiplication_1 = int(number1) * int(number2)
subtraction_1 = int(number1) - int(number2)

print(30*"-", 'results', 30*"-")

print('the result of sum numbers is:', plus_1 )
print('the result of division numbers is:', division_1)
print('the result of whole division numbers is:', whole_division_1)
print('the result of multiplication numbers is:', multiplication_1)
print('the result of subtraction numbers is:', subtraction_1)

'''
- - - - - - type of datas - - - - - -
float - real numbers, have ',', Ex: 1.5, 2.0, 3.14
int - integer numbers, have no ',' Ex: 1, 2, 3, 4
str - string, text, have '', Ex: 'hello', 'world'
bool - boolean, True or False
'''
print(90*"-")

year_of_birth_1 = input('put your year of birth:')
print(type(year_of_birth_1))
year_of_birth_1 = int(year_of_birth_1)  #transform string to int
print(type(year_of_birth_1))
