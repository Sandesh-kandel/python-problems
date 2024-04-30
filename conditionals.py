# age = int(input("Enter your age: "))
# day = 'Sunday'
# if age<14:
#     print("You are a child")
# elif age>14 and age<28:
#     print("You' are an adult")
# else:
#     print("you're old")

# what if users enters a neagtive age

while True:
    age_input = (input("ENter your age"))
    if age_input.isdigit():
        age= int(age_input)
        if age>=0:
            break
    print('Print enter a valid age.')
if age < 14:
    print("Child") 
elif age >14 and age <29: 
    print("Adult")
else:
    print("You are old")              