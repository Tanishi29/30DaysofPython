## learning strings in python 

letter = 't'
print(letter)


# multiline quotes are from """ or '''

first_name = 'tanishi'
last_name = 'kumar'
space = ' '
full_name= first_name + space + last_name
print(full_name)


# escape sequence: \n; \t; \\; \'; \"
# %s, %d, %f, %.numberofdigitsf (precision)
#str.format
# method 2: print(f'{a} + {b} = {a +b}')
#accessing strings is 0 indexed 
language = 'python'
first = language[0]
print(first)
end = language[-1]
print(end)
first_three = language[0:3] #starts from 0 ends before 3 (0, 1, 2)

#reverse 
print(language[::-1])
#capitalize() capitalizes the first letter of the string
#count() counts the occurance of a substring count(substr, start, end)
#endswith() checks if a string ends with a specific char/string
#expandtabs() replaces tab chars with spaces (8 = default)
#find() returns the index of the first occurance of a substring
#rfind() returns the index of the last occurance of a substring
#format(): sentence = 'I am {} {}. I am a {}. I am {} years old. I live in {}.'.format(first_name, last_name, job, age, country)
#isalnum() checks for alphanumeric character
#isalpha() checks if all string elements are alphabet
#isdecimal() checks for decimal
#isdigit()
#isnumeric() like digits but includes 1/2
#isidentifier checks if a string is a valid variable name
#islower() / #isupper()
#join() returns a concatenated string 
#strip(): removes specific sections of the string from the entire string 
#replace(): replaces a string with a different string
#split(): splits the string using a separator
#title(): returns the title version of the string
#swapcase(): swaps uppercse -> lowercase and vice versa
#startswith(): checks if a string starts with a specific string 

#EXERCISES: 

python = ['thirty', 'days', 'of', 'python']
res = ' '.join(python)
print(res)

company = 'Coding For All'
print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(company.swapcase())
print(company.title())
print(company.capitalize())
print(company[7:])

print(company.find('Coding'))
print(company.replace('Coding', 'Python'))
print(company.split(' '))

str1 = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(str1.split(', '))

print(company[0])
print(company[-1])
print(company[10])

print(company.index('C'))
print(company.index('F'))

str2 = 'You cannot end a sentence with because because because is a conjunction'
print(str2.find('because'))
print(company.rfind('l'))
print(str2.rfind('because'))

print(company.startswith('Coding'))
print(company.endswith('coding'))


str3 = 'You cannot end a sentence with because because because is a conjunction'
print(str3[31:47+len("because")+1])
print(str3.replace("because because because ",""))

print('   Coding For All      '.strip())

print('30DaysOfPython'.isidentifier())
print('thirty_days_of_python'.isidentifier())

list1 = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(" ".join(list1))

print('I am enjoying this challenge.\nI just wonder what is next.')

radius = 10
area = 3.14 * radius ** 2
formatstring = 'The area of the circle with a radius {} is {:.2f}.'.format(radius, area)
print(formatstring)


name = 'shruti'
age = 20
country = 'USA'
city = 'Phoenix' 

print('Name\tAge\tCountry\tCity')
print('{}\t{}\t{}\t{}'.format(name, age, country, city))

a = 8
b = 6

print(f'{a} + {b} = {a+b}')
print(f'{a} - {b} = {a-b}')
print(f'{a} * {b} = {a*b}')
print(f'{a} / {b} = {a/b:.2f}')
print(f'{a} % {b} = {a%b}')
print(f'{a} // {b} = {a//b}')
print(f'{a} ** {b} = {a**b}')

