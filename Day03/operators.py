
# DAY 03: OPERATORS

import math

age = 20
height = 170.0
weight = 1 + 1j

base = input('Enter the base: ')
height = input('Enter the height: ')

area_triangle = 0.5 * float(base) * float(height)
print('The area of the triangle is ', area_triangle)

a = input('Enter side a: ')
b = input('Enter side b: ')
c = input('Enter side c: ')
perimeter_triangle = float(a) + float(b) + float(c)
print('The perimeter of the triangle is ', perimeter_triangle)


r = input('Enter radius: ')
circumference = float(2) * float(r) * math.pi
print(circumference)


m1 = 2
m = (10-6) / (6-2)
print(m1 == m)

x = 3
y = x**2 + 6*x + 9
print('y is: ', y)

e = len('python')
f = len('dragon')
print(e != f)

print('on' not in 'python' and  'on' not in 'dragon')

print(float(e))
print(str(e))


# checking if a number is even or no, the remainder is 0 if even and != 0 if odd
num = input('enter a num: ')
remainder = int(num) % 2
print('your remainder is: ', remainder)

print((7//3) == int(2.7))

print(type('10') == type(10))
print(int(float('9.8')) == 10)

hours = input('enter hours: ')
rate = input('enter rate per hour: ')
earning = int(hours) * int(rate)
print('your weekly earning is ', earning)

years = input('enter years you lived: ')
seconds = int(years) * 31556926
print('you lived ', seconds, 'seconds.')



print(f"{'a':<5} {'a^0':<5} {'a^1':<5} {'a^2':<5} {'a^3':<5}")

# Loop through base numbers 1 to 5
for a in range(1, 6):
    # Calculate the powers for each column
    p0 = a ** 0
    p1 = a ** 1
    p2 = a ** 2
    p3 = a ** 3
    
    # Print the row with a fixed left-aligned width of 5 characters per column
    print(f"{a:<5} {p0:<5} {p1:<5} {p2:<5} {p3:<5}")





