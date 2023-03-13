#include <iostream>
using namespace std;
int main()
{
	double a, b;
	cout << "Podaj wspolczynnik a: ";
	cin >> a;
	cout << "Podaj wyraz wolny b: ";
	cin >> b;
	cout << "Funkcja przyjmuje postać: y = " << a << "x + " << b << endl;

	double start, end;
	cout << "Podaj dziedzine funkcji" << endl;
	cout << "Podaj poczatek dziedziny:";
	cin >> start;
	cout << "Podaj koniec dziedziny:";
	cin >> end;
	if (end > start) {
		if (a == 0 && b == 0)
		{
			cout << "Funkcja jest tozsamosciowa" << endl;
		}
		else {
			// zbior wartosci funkcji
			double yMin, yMax;
			if (a > 0) {
				yMin = start * a + b;
				yMax = end * a + b;
				cout << "Zbior wartosci y to:(" << yMin << ";" << yMax << ")" << endl;
			}
			if (a < 0) {
				yMin = end * a + b;
				yMax = start * a + b;
				cout << "Zbior wartosci y to:(" << yMin << ";" << yMax << ")" << endl;
			}
			if (a == 0) {
				cout << "Zbior wartosci to punkt b = (" << b << ")" << endl;
			}
			// miejsce zerowe
			double mscZero;
			if (a != 0) {
				mscZero = -b / a;
				cout << "Miejsce zerowe to: " << mscZero << endl;

			}
			else {
				cout << "Brak miejsca zerowego" << endl;
			}
			// monotonicznosc
			if (a > 0) {
				cout << "Funkcja jest rosnaca" << endl;
			}
			if (a < 0) {
				cout << "Funkcja jest malejaca" << endl;
			}
			if (a == 0) {
				cout << "Funkcja jest stala." << endl;
			}
			// wartosci dodatnie
			if (a > 0) {
				cout << "Funkcja przyjmuje wartosci dodatnie dla x =(" << mscZero << ";" << end << ")" << endl;
			}
			if (a < 0) {
				cout << "Funkcja przyjmuje wartosci dodatnie dla x =(" << start << ";" << mscZero << ")" << endl;
			}
			if (b > 0 && a == 0) {
				cout << "Funkcja przyjmuje wartosci dodatnie dla x =(" << start << ";" << end << ")" << endl;
			}
			if (a == 0 && b < 0) {
				cout << "Funkcja nie ma wartosci dodatnich" << endl;
			}
			// wartosci ujemne
			if (a > 0) {
				cout << "Funkcja przyjmuje ujemne dla x =(" << start << ";" << mscZero << ")" << endl;
			}
			if (a < 0) {
				cout << "Funkcja przyjmuje wartosci ujemne dla x =(" << mscZero << ";" << start << ")" << endl;
			}
			if (b < 0 && a == 0) {
				cout << "Funkcja przyjmuje wartosci ujemne dla x =(" << start << ";" << end << ")" << endl;
			}
			if (a == 0 && b > 0) {
				cout << "Funkcja nie ma wartosci ujemnych" << endl;
			}
			// punkt przeciecia z osia Y
			cout << "Punkt przeciecia z osia Y to punkt: " << b << endl;
			// argument dla danej wartosci
			double wartosc;
			cout << "Wpisz wartosc dla ktorej chcesz policzyc argument: ";
			cin >> wartosc;
			if (a > 0) {
				if (start * a + b <= wartosc <= end * a + b)
				{
					cout << "Argument x dla wartosci y wynosi: " << b - wartosc / -a << endl;
				}
				else {
					cout << "Podana wartosc jest poza zbiorem wartosci. " << endl;
				}
			}
			if (a < 0) {
				if (start * a + b >= wartosc >= end * a + b)
				{
					cout << "Argument x dla wartosci y wynosi: " << b - wartosc / -a << endl;
				}
				else {
					cout << "Podane wartosc jest poza zbiorem wartosci" << endl;
				}
			}
			// wartosc dla podanego argumentu
			double argument;
			cout << "Wpisz argument dla ktorego chcesz policzyc wartosc: ";
			cin >> argument;
			if (start <= argument && argument <= end) {
				cout << "Wartosc dla podanego argumentu wynosi: " << argument * a + b << endl;
			}
			if (!(start <= argument && argument <= end)) {
				cout << "Podany argument jest poza dziedzina." << endl;
			}
			cout << "Program zakonczyl dzialanie";
		}
	}
	else {
		"Wprowadziles niepoprawne dane";
	}

	return 0;
}