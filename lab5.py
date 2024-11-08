'''
print('Cw1\n')
#a
def gmean(*args):
    ilosc = len(args)
    for arg in args:
        wynik = arg*arg
    return wynik

gmean(3,6,3,2)
'''
#b
'''
def func(*args):
    for i in range(1,len(args)+1):
        print(' '.join(map(str, args[:i])))
func(3,'Ala',5)
'''
#c
'''
def func(*args):
    for arg in args:
        print(' '.join([str(arg)]*arg))
func(3,'Ala',5)
'''
print('Cw2\n')
#a

def my_max1 (*args):
    if a==b:
        return print('Obie liczby są równe.')
    elif a<b:
        return print('Wieksza jest liczba: ',b)
    else:
        return print('Wieksza jest liczba: ',a)
a = float(input("Podaj liczbę A: "))
b = float(input("Podaj liczbę B: "))
my_max1 (a, b)
#b

#def my_max2(a, b, c):


#c



