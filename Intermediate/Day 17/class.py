# Creating a class
# Class names should be pascal cased
class User:
    # init function will be called everytime an object is created
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        # default value
        self.followers = 0
        self.following = 0

#     adding methods to a class
    def follow(self, user):
        user.followers += 1
        self.following += 1


# user_1 = User()
# # How to create an attribute to a class?
# user_1.id = "001"
# user_1.username = "Dev"
# print(user_1.username)
user_1 = User("001", "Dev")
user_2 = User("002", "Zeno")
print(user_2.username)

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)

# Constructor: a part of the blueprint -- initializing an object
# def __init__(self):


# If we just want an  empty class or function we can use the keyword "pass"
# def my_function():
#     pass
#
# print("Hello!")
