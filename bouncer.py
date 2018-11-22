# # ask for age
# age = input("What is your age?")
# # under 18
# if age < 18: 
# 	print("You cannot enter.")
# # 18 - 21
# elif age >= 18 and age < 21:
# 	print("You can enter, but you cannot drink.")
# # over 21
# elif age >= 21:
# 	print("Come on in, and have a drink!")
# else:
# 	print("Please enter age.")

# Bouncer Code 

# ask for age
age = input("What is your age?")
if age:
	age = int(age) 
	if age >= 21:
		print("Come on in and have a drink!")
	elif age >= 18:
		print("You can enter, but you cannot drink.")
	else: 
		print("You cannot enter. Sorry kiddo.")
else:
	print("Please enter your age.")

# Coding exercise

if x > 0 and y > 0:
	print("both positive")
elif x < 0 and y < 0:
	print("both negative")
elif x > 0 and y < 0:
	print("x is positive and y is negative")
else:
	print("y is positive and x is negative")

# Calling In Sick Exercise:

if actually_sick and int(sick_days) > 0:
	calling_in_sick = True
elif kinda_sick and hate_your_job and int(sick_days) > 0:
	calling_in_sick = True
else: 
	calling_in_sick = False

