
age = int(input("enter your age: "))



if age >= 19 :
    print("you dont get a discount")
elif age < 19:
    print("you get a 10% discount in my shop")
else:
    print("sorry you dont get a discount")

age = int(input("enter your age: "))

if age >= 18 and age <= 40:
    print("you can work here")
else:
    print("sorry you cant work here")

play = input("do you want to play? ")

if play == "yes":
    print("lets play")
else:
    print("okay we can do something else")


num = 1

for i in range(5):
    print(num)
    num = num + 6