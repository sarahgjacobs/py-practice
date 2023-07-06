import random

num = input("Pick a random number ")

if num.isdigit():
    num = int(num)
    if num <= 0:
        print('please choose a higher number')
        quit()
    else:
        print('please print a number')



r = random.randrange(0, 10)

