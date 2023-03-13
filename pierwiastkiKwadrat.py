from math import sqrt
def pierwiastki(a,b,c):
    delta = (b*b - (4 * a * c))
    pierwDelta = round(sqrt(abs(delta)),2)
    if delta > 0:
        x1 = -b + pierwDelta / (-2 * a)
        x2 = -b + -pierwDelta / (-2 * a)
        print(f"Funkcja posiada dwa miejsca zerowe x\u2081 = {round(x1,2)}, x\u2082 = {round(x2,2)}")
    elif delta == 0:
        x0 = -b / -2 * a
        print(f"Funkcja posiada jedno miejsce zerowe x\u2080 = {round(x0,2)}")
    else:
        x1 = f"{round(-b / (-2 * a),2)}{round(pierwDelta / (-2 * a),2):+}i"
        x2 = f"{round(-b / (-2 * a),2)}{round(-pierwDelta / (-2 * a),2):+}i"
        print(f"Delta ujemna, operacja na liczbach zespolonych, x\u2081 = {x1}, x\u2082 = {x2}")
try:
    print(f"Funkcja kwadratowa przyjmuje nastepujaca postac: ax\u00b2 + bx + c")
    x,y,z = [float(a) for a in input("Podaj wartosci a,b,c. Pamiętaj, aby oddzielic je przcinkiem: ").split(",")]
    if x == 0:
        print("Wspolczynnik kierunkowy 'a' musi być różny od 0!")
        raise ValueError
    else:
        pierwiastki(x,y,z)
except ValueError:
    print("Podales niepoprawne wartosci do strumienia. Program zakonczyl swoje dzialanie")