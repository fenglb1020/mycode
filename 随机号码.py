import random, os

def z500w():
    list_x = []
    list_y = []
    while True:
        if len(list_x) == 6:
            break
        x = random.randint(1, 33)
        if x in list_x:
            continue
        list_x.append(x)

    list_y.append(random.randint(1, 16))

    list_x.sort()
    list_y.sort()

    with open('a.txt', 'a') as f:
        f.writelines('红球：' + str(list_x)+'\n')
        f.writelines('蓝球：' + str(list_y)+'\n')

for i in range(3):
    z500w()