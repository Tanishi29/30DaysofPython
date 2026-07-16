#DAY 2: VARIABLES 

#EXERCISE 1: DECLARE VARIABLES

import math

first_name = 'Tanishi'
last_name = 'Kumar'
full_name = first_name + ' ' + last_name
country = 'India'
city = 'Pune'
age = 20
year = 2026
is_married = False
is_true = True
is_light_on = False

curr_city, country, favorite_food = 'Phoneix', 'USA', 'Pizza'


#EXERCISE 2: DATA TYPES
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(curr_city))
print(type(favorite_food))   

print(len(first_name))
print(len(first_name) == len(last_name))

num_one = 5
num_two = 4
total = num_one + num_two
diff = num_two - num_one
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two
exp = num_one ** num_two
floor_division = num_one // num_two

radius = 30; 
area_of_circle = (math.pi) * radius ** 2
circumference_of_circle = 2 * math.pi * radius
print(area_of_circle)
print(circumference_of_circle)

user_rad = input("Enter radius of circle: ")
area_of_circle = (math.pi) * int(user_rad) ** 2
circumference_of_circle = 2 * math.pi * int(user_rad)
print(area_of_circle)
print(circumference_of_circle)

user_first_name = input("Enter your first name: ")
user_last_name = input("Enter your last name: ")
user_age = input("Enter your age: ")
user_country = input("Enter your country: ")

print(user_first_name + ' ' + user_last_name + ' is ' + user_age + ' years old and lives in ' + user_country)



