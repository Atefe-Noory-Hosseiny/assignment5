import random
n=int(input("How long is list:"))
number_list=[]

for i in range(n):
    number=random.randint(0,1000)
    if number not in number_list:
        number_list.append(number)

print(number_list)