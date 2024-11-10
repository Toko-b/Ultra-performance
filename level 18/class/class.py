

num = []

for i in range(1, 11):
    num.append(i)

print(num)
print(len(num))

count = int(input("please enter a number: "))
count2 = int(input("please enter a number: "))
num = []

for i in range(count, count2):
    num.append(i)

print(num)
print(len(num))

first_num = int(input("please enter a number: "))
last_num = int(input("please enter a number: "))
num = []


for i in range (first_num, last_num):
    num.append(i)

print(num)
print(min(num))
print(max(num))
print(sum(num))

count = int(input("please enter a number: "))

numbers = []

for i in range(count):
    num = int(input("please enter a number: "))
    numbers.append(num)

print(numbers)
print(sum(numbers))

cars = ['ferrari', 'bmw', 'nissan', 'pagani', 'keoninsegg']

print(cars[4:6])

cars = ['ferrari', 'bmw', 'nissan', 'pagani', 'keoninsegg']
sliced_list = cars[:3]
last_two = cars[-2:]

print(last_two)
print(sliced_list)


print(cars[-3])
print(cars[-4])

list = ["tornike"]

user_name = [input("enter your name: ")]

if user_name == list :
    print("hello admin")
else:
    print("hello user")