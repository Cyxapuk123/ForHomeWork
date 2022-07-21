import random
my_list = []
for i in range(1000):
    my_list.append(random.randint(-1000, 1000))

my_list.sort()
print(my_list[0])
