def mscZero(a,b,start,end):
    if a != 0:
        x0 = round(-b/a,2)
        if start <= x0 <= end:
            print(f"Miejsce zerowe to {x0}")
            return x0
        else:
            print("Brak miejsca zerowego")
            return None 
    else:
        print("Brak miejsca zerowego")
        return None 
def monotFun(a):
    if a > 0:
        print("Funkcja jest rosnaca")
    elif a < 0:
        print("Funkcja jest malejaca")
    else:
        print("Funkcja jest stala")
def zbiorWar(a,b,start,end):
    if a == 0:
        print(f"Zbiorem wartosci jest punkt {b}")
    elif start == float('-inf') and end == float('inf'):
        print("Zbior wartosci jest nieskoczony")
    elif a > 0:
        if start == float('-inf'):
            print(f"Zbior wartosci funkcji to (-nieskonczonosc;{a * end + b})")
        elif end == float('inf'):
            print(f"Zbior wartosci funkcji to ({a * start + b};+nieskoncznonosc)")
        else:
            print(f"Zbiór wartości funkcji nalezy do y:({a*start+b};{a*end+b})")
    elif a < 0:
        if start == float('-inf'):
            print(f"Zbior wartosci funkcji to (-nieskonczonosc;{a * end + b})")
        elif end == float('inf'):
            print(f"Zbior wartosci funkcji to ({a * start + b};+nieskoncznonosc)")
        else:
            print(f"Zbiór wartości funkcji nalezy do y:({a*end+b};{a*start+b})")
def dodatnie(a,b,start,end,zero):
    if a == 0 and b > 0:
        print(f"Funkcja przyjmuje wartosci dodatnie dla x = {b}")
    elif  a == 0 and b < 0:
        print("Brak wartosci dodatnich")
    elif a > 0:
        if zero != None:
            print(f"Funkcja przyjmuje wartości dodatnie dla x należacych do:({zero};{end})")
        elif zero == None and a * start + b > 0:
            print(f"Funkcja przyjmuje wartości dodatnie dla x należacych do:({start};{end})")
        else:
            print("Brak wartosci dodatnich")
    elif a < 0:
        if zero != None:
             print(f"Funkcja przyjmuje wartości dodatnie dla x należacych do:({start};{zero})")
        elif zero == None and a * end + b > 0:
            print(f"Funkcja przyjmuje wartości dodatnie dla x należacych do:({start};{end})")
        else:
            print("Brak wartosci dodatnich")
def ujemne(a,b,start,end,zero):
    if a == 0 and b > 0:
        print("Brak wartosci ujemnych")
    elif  a == 0 and b < 0:
        print(f"Funkcja przyjmuje wartosci ujemne dla x = {b}")
    elif a > 0:
        if zero != None:
            print(f"Funkcja przyjmuje wartości ujemne dla x należacych do:({start};{zero})")
        elif zero == None and a * end + b < 0:
            print(f"Funkcja przyjmuje wartości ujemne dla x należacych do:({start};{end})")
        else:
            print("Brak wartosci ujemnych")
    elif a < 0:
        if zero != None:
             print(f"Funkcja przyjmuje wartości ujemne dla x należacych do:({zero};{end})")
        elif zero == None and a * start + b < 0:
            print(f"Funkcja przyjmuje wartości ujemne dla x należacych do:({start};{end})")
        else:
            print("Brak wartosci ujemnych")
def pktPrzeciecia(a,b,start,end):
    if a > 0 and start <= 0 <= end:
        print(f"Miejsce przeciecia z osią Y to {b}")
    elif a < 0 and start >= 0 >= end:
        print(f"Miejsce przeciecia z osią Y to {b}")
    elif a == 0:
        print(f"Miejsce przeciecia z osią Y to {b}")
    else:
        print("Funkcja nie przecina osi Y")
def argDlaWartosci(a,b,start,end):
    try:
        wartosc = float(input("Podaj wartosc Y dla ktorego chcesz policzyc jego x: "))
        if a < 0 and a * start + b >= wartosc >= a * end + b:
            x = b - wartosc / -a
            print(f"Argument o wartości {wartosc} wynosi {x}")
        elif a > 0 and a * start + b <= wartosc <= a * end + b:
            x = b - wartosc / -a
            print(f"Argument o wartości {wartosc} wynosi {x}")
        elif a == 0:
            print("Funkcja jest stała")
        else:
            print("Podana wartosc jest poza zbiorem")
    except ValueError:
        print("Wprowadziles zle dane. Podany argument jest poza dziedzina.")
def wartoscDlaArg(a,b,start,end):
    try:
        x = float(input("Podaj arg X dla ktorego chcesz policzyc jego Y: "))
        if a < 0 and start >= x >= end:
            y = a * x + b
            print(f"Argument {x} przyjmuje wartosc {y}")
        elif a > 0 and start <= x <= end:
            y = a * x + b
            print(f"Argument {x} przyjmuje wartosc {y}")
        elif a == 0:
            print("Funkcja jest stała i posiada jedna wartosc.")
        else:
            print("Podany argument jest poza dziedzina")
    except ValueError:
        print("Wprowadziles zle dane. Podana wartosc jest poza zbiorem wartosci")
try:
    a, b = [float(a) for a in input("Funkcja liniowa jest w postaci y = ax + b, wprowadz a oraz b oddzielajac dane przecinkiem: ").split(",")]
    if a == 0 and b == 0:
        print("Funkcja tożsamościowa. Program zakończony. ")
    else:
        print(f"Funkcja ma postać y = {a}x + {b}")
        ask = input("Czy chcesz podac dziedzine funkcji(domyślnie -niesk;+niesk)? Odpowiedz wpisujac 'tak' lub 'nie': ").replace(" ","").lower()
        if ask == "tak":
            xMin,xMax = [float(a) for a in input("Podaj dziedzine funkcji - poczatek oraz koniec. UWAGA, dane oddziel przecinkiem(inf = +niesk., -inf = -niesk.): ").replace(" ","").split(",")]
            if xMin > xMax:
                raise ValueError
        elif ask == "nie":
            xMin = float('-inf')
            xMax = float('inf')
        else:
            raise ValueError
        # wykonanie programu
        xzero = mscZero(a,b,xMin,xMax)
        monotFun(a)
        zbiorWar(a,b,xMin,xMax)
        dodatnie(a,b,xMin,xMax,xzero)
        ujemne(a,b,xMin,xMax,xzero) 
        pktPrzeciecia(a,b,xMin,xMax)
        argDlaWartosci(a,b,xMin,xMax)
        wartoscDlaArg(a,b,xMin,xMax)
        print("Program zakonczyl swoje działanie. ")


except ValueError:
    print("Wprowadzone dane są nieprawidłowe. Pamietaj aby podac dokladnie 2 dane(pierwsza mniejsza od drugiej) i oddzielic je przecinkiem oraz konkretnie udzielic odpowiedzi na pytanie. \n Program zakończył swoje działanie")