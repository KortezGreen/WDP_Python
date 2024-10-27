print('Cw1\n')
'''
    Iteracja 1: i = 1, s = 1 * 1 = 1
    Iteracja 2: i = 2, s = 1 * 2 = 2
    Iteracja 3: i = 3, s = 2 * 3 = 6
    Iteracja 4: i = 4, s = 6 * 4 = 24
    Iteracja 5: i = 5, s = 24 * 5 = 120

Wartości zmiennych i i s w każdej iteracji pętli for to:

    Iteracja 1: i = 1, s = 1
    Iteracja 2: i = 2, s = 2
    Iteracja 3: i = 3, s = 6
    Iteracja 4: i = 4, s = 24
    Iteracja 5: i = 5, s = 120
'''
'''
    Początkowe wartości: a = 1, c = 0
    
    Iteracja pętli while: a = 1

        Iteracja for: b = 1, c = 0 + (1 + 1 + 1) = 3
        Iteracja for: b = 2, c = 3 + (1 + 2 + 1) = 7
        Po pętli for: c = 7 + 8 = 15
        Aktualizacja: a = 2

    Iteracja pętli while: a = 2

        Iteracja for: b = 1, c = 15 + (2 + 1 + 1) = 19
        Iteracja for: b = 2, c = 19 + (2 + 2 + 1) = 24
        Po pętli for: c = 24 + 8 = 32
        Aktualizacja: a = 3
'''

print('Cw2\n')
# a
'''
def dziel():
    a = float(input("Podaj dzielną: "))
    b = float(input("Podaj dzielnik: "))
    wynik_dziel=a/b
    print('Wynik to: ', wynik_dziel)

dziel()
'''
# b
'''
def konwenter():
    a = float(input("Podaj temperaturę: "))
    b = str(input("F czy C? -> "))
    if b == 'C':
        print((a * 1.8) + 32)
    elif b == 'F':
        print((a - 32) / 1.8)
    else:
        print('Nie podano C ani F!')
konwenter()
'''
print('Cw3\n')
# a
'''
def lnum(n):
    if n == 0:
        return 1
    sumal = 0
    while n > 0:
        n = n // 10
        sumal += 1
    print('Ilość cyfr wynosi: ', sumal)
n = int(input("Podaj liczbę do liczenia cyfr: "))
lnum(n)
'''
# b
'''
def pierwsza(p):
    if p <= 1:
        return 0
    for i in range(2, int(p ** 0.5) + 1):
        if p % i == 0:
            return 0
    return 1
p = int(input("Podaj liczbę: "))
if pierwsza(p) == 1:
    print('Pierwsza')
else:
    print('Nie pierwsza')
'''
print('Cw4\n')
'''
import cmath
def kwadrat(a, b, c):
    if a == 0:
        if b == 0:
            if c == 0:
                return "Równanie tożsamościowe"
            else:
                return "Brak rozwiązań"
        else:
            return f"Równanie liniowe, rozwiązanie: x = {-c / b}"

    delta = b**2 - 4*a*c

    if delta > 0:
        x1 = (-b + cmath.sqrt(delta)) / (2*a)
        x2 = (-b - cmath.sqrt(delta)) / (2*a)
        return f"Rozwiązania rzeczywiste: x1 = {x1.real}, x2 = {x2.real}"
    elif delta == 0:
        x = -b / (2*a)
        return f"Jedno podwójne rozwiązanie: x = {x}"
    else:
        x1 = (-b + cmath.sqrt(delta)) / (2*a)
        x2 = (-b - cmath.sqrt(delta)) / (2*a)
        return f"Rozwiązania zespolone: x1 = {x1.real} + {x1.imag}i, x2 = {x2.real} + {x2.imag}i"

a = float(input("Podaj wartość a: "))
b = float(input("Podaj wartość b: "))
c = float(input("Podaj wartość c: "))
wynik = kwadrat(a, b, c)
print(wynik)
'''
print('Cw5\n')
'''
def sgn(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0

liczba = float(input("Podaj liczbę zmiennoprzecinkową: "))
znak = sgn(liczba)
print(f"Znak podanej liczby to: {znak}")
'''
print('Cw6\n')
#e1
'''
def oblicz1(n):
    wynik_e1=(1+1/n)**n
    return print('Wynik to :',wynik_e1)
n = int(input("Podaj liczbę n: "))
oblicz1(n)
'''
#e2
'''
def silnia(k):
    if k == 0:
        return 1
    wynik = 1
    for i in range(1, k + 1):
        wynik *= i
    return wynik

def suma(n):
    suma = 0
    for k in range(n + 1):
        suma += 1 / silnia(k)
    return suma


n = int(input("Podaj liczbę całkowitą n: "))
wynik = suma(n)
print(f"Suma dla n = {n} wynosi: {wynik}")
'''
