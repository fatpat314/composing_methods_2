# By Kami Bigdely
# Split temp variable

def save_into_db(info):
    print("saved into databse")


user_input_name = input('Please enter your username: ')
save_into_db(user_input_name)
user_input_age = int(input('Please enter your birth year: '))
age = 2020 - user_input_age
print("You are",age, "years old.")