'''

  Data types
  1. integer; int()
  2. floating point; float()
  3. boolean; bool()
  4. string; str()




num = 4
# I am 4 years old
print("I am " + str(num) + " years old")


Variable name
 1. Must start with a letter
 2. No symbols except _
 3. numbers, letters can follow after the first letter
 4. No space at all


 01/21/2021
 Operations

 1. Math Operators (Arithmetic Operatiors)
 Additon, +
 Subtraction, -
 Multiplicaton, *
 Divison, /
Modulo, % (Remainder)
Exponent, ** (power)

5/2= 2.5
5//2= 2
5 % 2= 1
1 % 3= 1
2 % 3= 2
3 % 3= 0
10 % 2= 0
11 % 2= 1
2 ** 2= 4
3 ** 4= 81



2. Assignment Operators
-Used to assign values to variables

-Rule Using Assignment Operators
 A variable must be declared before using assignment opreators with the variable


variable = data/value
variable = input(prompt)

0. Simple Assignment, =
1. Addition Assignment, +=
  A += B
  A = A + B
2. Subraction Assignment, -=
  A -= B
  A = A - B
3. Multiply Assignment, *=
4. Divide Assignment, /=
5.Modulo Assignment, %=
6.Exponent Assignment, **=

Ex)
a = 5
a += 2 # Equivalent to: 



a = 5
a += 2 # a = a+ 2
print("I am " + str(a))



3. Comparison Operators (Relational Operators)
-Used to compare values for conditions, Returns booleans after evaluation. 
-Rule: Using Comparsion Operators
  Two objects are required such as a variable or a raw data/value
  a. equal to, ==
  b. not equal to, !=
  c. less than, <
  d. less than or equal to, <=
  e. greater than, >
  f. greater than or equal to, >=
'''

a = 8
while (a<10):
  print(a)
  a += 1  # a = a+1

# Math Operators (Arithmetic Operatos)
x = 7
y = 2

# x + y = 7+2=9
print("x+y = " + str(x+y))

x1=5
x2=3

x1 += 7 #x1= x1+7 x1=12
print(x1)


x1 -= x2 #x1=x1-x2 = x1=12-3 = 9
print(x1)

x2 *= 2 #x2=x2*2
print(x2)

x2 /= 3 #x2=x2/3
print(x2)

x1 %= 7 #x1=x1%7
print(x1)
