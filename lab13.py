#ćw 2
#a)
# import random
# for x in range(99):
#     l = x = random.randint(-100, 100)
#     print(l)
#     if l % 2 == 0:
#             dod = open("dodatnie.txt", "a")
#             dod.write(str(l) + ' ')
#             dod.close()
#     else:
#             uj = open("ujemne.txt", "a")
#             uj.write(str(l) + ' ')
#             uj.close()
#b)

with open("dodatnie.txt", "r") as dod1:
    lis1 = dod1.read()
    lis2 = [int(x) for x in lis1.split()]
    suma = sum(lis2)
    print('Suma parzystych to:',suma)

with open("ujemne.txt", "r") as uj1:
    lis3 = uj1.read()
    lis4 = [int(x) for x in lis3.split()]
    suma2 = sum(lis4)
    print('Suma nieparzystych to:',suma2)

print('Suma obu to:',suma+suma2)
