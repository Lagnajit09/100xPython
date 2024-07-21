############DEBUGGING#####################

# # Describe Problem
# def my_function():
#   # Bug: range() doesnt include upperbound
#   # for i in range(1, 20):
#   for i in range(1, 21):
#     if i == 20:
#       print("You got it")
# my_function()

# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# # Bug: the indices starts from 0 to len-1
# # dice_num = randint(1, 6)
# dice_num = randint(0, 5)
# print(dice_imgs[dice_num])

# # Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# # no block for 1994
# # elif year > 1994:
# elif year >= 1994:
#   print("You are a Gen Z.")

# # Fix the Errors
# # int cant be compared with str
# # age = input("How old are you?")
# age = int(input("How old are you?"))
# if age > 18:
#   # To print the age we need f string
#   # print("You can drive at age {age}.")
#   print(f"You can drive at age {age}.")

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))

# # == used for comparison while = used for assigment
# # word_per_page == int(input("Number of words per page: "))
# word_per_page = int(input("Number of words per page: "))

# # debug: print statement
# print(pages, word_per_page)
# total_words = pages * word_per_page
# print(total_words)

# #Use a Debugger
# # https://pythontutor.com/python-compiler.html#mode=edit
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#   # it should be indented to append all the items in the new list
#   # b_list.append(new_item)
#     b_list.append(new_item)
    
#   print(b_list)

# mutate([1,2,3,5,8,13])