
# msg = "Hello World"
# print(msg)

#comments are just '#' hashed out 

# greeting = "Welcome, "
# name = input('Tell me your name: ')
# age = input('How old are you?')
# goals = input('What do you want to get out of learning Python?')
# print(greeting + name, 'you are', age, '.')

# We will calculate the area of a circle

# radius = input('What is the radius of your circle?  ')
# answer = 3.14 * int(radius)**2
# print('The area of your circle is', answer)

# num1 = 3.14
# num2 = 202.902

# PREVIOUS
# print('num1 is', num1, 'and num2 is', num2)

# FORMAT METHOD
# print('num 1 is {0} and num 2 is {1}'.format(num1, num2))

# USING F-STRINGS
# print(f'num 2 is {num1} and num 2 is {num2}')

# IF STATEMENTS-----------
# age = int(input('Enter your age:'))
# if age < 10:
#     print('You are under 10 years old')
# elif age < 20:
#     print('You are older than ten but less than twenty years old')
# else: 
#     print('You are an old person')

# veggie = input('Are you a vegetarian? (y/n)')

# if veggie == 'y':
#     print("Here is the vegetarian menu")
# elif veggie == 'n':
#     print("Here are is the meat eaters menu")
# else: 
#     print('Please try again')

# # FOR LOOPS-------------
# ballers = ['Kobe', 'MJ', 'Lebron', 'KD', 'Steph']

# # for player in ballers:
# #     print(player, "is a baller")

# for baller in ballers:
#     if baller == "Kobe":
#         print(f"{baller} is an all time Great")
#     elif baller == "MJ":
#         print(f'{baller} is the G.O.A.T')
#     else:
#         print(f'{baller} is great at basketball')



# array = [1, 2, 3, 4]

# WHILE LOOPS ----------------

age = 25
num = 0

while num < age:
    if num % 2 ==0:
        print(num)
    num += 1