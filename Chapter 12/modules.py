from math import sqrt
import datetime
import random
import readtime

print('hello world')


print(sqrt(16))
# print(math.pi)
# print(math.pow(2, 3))

print(datetime.datetime.today())

my_students = ['John', 'Samuel', 'Jane']
print(random.choice(my_students))

result = readtime.of_text('The shortest blog post in the world! gfhjhkjnl;jhgfghjklkjhgcvbnkhgfdddddddddddddddddddddddddddddddddd')
print(result.seconds)