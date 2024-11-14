'''
print('Cw1\n')
#a
def gmean(*args):
    wynik1 = 1
    for liczba in args:
        wynik1 *= liczba
    return wynik1 ** (1 / len(args))
gmean(2,4,5)
'''
#b
'''
def func(*args):
    for i in range(1, len(args) + 1):
        print(" ".join(map(str, args[:i])))
func(3, ’Ala’, 5)
'''
#c
'''
def func(*args):
    for i, arg in enumerate(args):
        print(" ".join([str(arg)] * (i + 1)))
func(3,'Ala',5)
'''
print('Cw2\n')
#a

def my_max1 (a,b):
    if a==b:
        return print('Obie liczby są równe.')
    elif a<b:
        return print('Wieksza jest liczba: ',b)
    else:
        return print('Wieksza jest liczba: ',a)
my_max1 (5, 4)

#b
def my_max2(a, b, c):
    if a==b==c:
        return print('Liczby są równe.')
    elif a<=b<c:
        return print('Wieksza jest liczba: ',c)
    elif a>b>=c:
        return print('Wieksza jest liczba: ',a)
    else:
        return print('Wieksza jest liczba: ',b)
my_max2 (5, 4, 7)

#c
def my_max3(*args):
    return max(args)
my_max3 (2,6,8,1)

print('Cw3\n')
#a
dodawania = 0

def fibonacci(n):
    global dodawania
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        dodawania += 1
        return fibonacci(n-1) + fibonacci(n-2)

def oblicz_fibonacci(n):
    global dodawania
    dodawania = 0
    wynik = fibonacci(n)
    return wynik

def main():
    liczby = [10, 29, 100]
    for n in liczby:
        wynik = oblicz_fibonacci(n)
        print(f"F({n}) = {wynik}, liczba dodawań: {dodawania}")

if __name__ == "__main__":
    main()


#b
dodawania = 0

def fibonacci(n):
    global dodawania
    a, b = 0, 1
    if n == 0:
        return a
    for _ in range(2, n + 1):
        a, b = b, a + b
        dodawania += 1
    return b

def oblicz_fibonacci(n):
    global dodawania
    dodawania = 0
    wynik = fibonacci(n)
    return wynik

def main():
    liczby = [10, 29, 100]
    for n in liczby:
        wynik = oblicz_fibonacci(n)
        print(f"F({n}) = {wynik}, liczba dodawań: {dodawania}")

if __name__ == "__main__":
    main()


print('Cw4\n')
#a
def euklides(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def main():
    print("NWD(56, 98):", euklides(56, 98))
    print("NWD(48, 180):", euklides(48, 180))
    print("NWD(101, 103):", euklides(101, 103))
    print("NWD(0, 25):", euklides(0, 25))
    print("NWD(25, 0):", euklides(25, 0))
    print("NWD(101, 101):", euklides(101, 101))

if __name__ == "__main__":
    main()


#b
def nieskracalny_ulamek(a, b):
    nwd = euklides(a, b)
    p = a // nwd
    q = b // nwd
    return p, q

def main():
    print("Nieskracalny ułamek dla 6/8:", nieskracalny_ulamek(6, 8))
    print("Nieskracalny ułamek dla 15/25:", nieskracalny_ulamek(15, 25))
    print("Nieskracalny ułamek dla 100/250:", nieskracalny_ulamek(100, 250))
    print("Nieskracalny ułamek dla 7/9:", nieskracalny_ulamek(7, 9))
    print("Nieskracalny ułamek dla 20/50:", nieskracalny_ulamek(20, 50))

if __name__ == "__main__":
    main()


print('Cw5\n')
#a
def liczba_zer_na_koncu(n):
    licznik = 0
    while n >= 5:
        n //= 5
        licznik += n
    return licznik
