import argparse
import random
import time
from datetime import datetime, timedelta


def pobierz(pytanie=""):
    while True:
        try:
            z = int(input(pytanie))
            return z
        except ValueError:
            print("Błąd odczytu, spróbuj jeszcze raz")


def podaj_wynik(s: int, czekaj: bool = True):
    print("Masz", s, "punktów", end="")
    if czekaj:
        print(", przygotuj się", end=" ", flush=True)
        for i in range(3):
            print(".", end=" ", flush=True)
            time.sleep(1)
    print()


parser = argparse.ArgumentParser()

parser.add_argument(
    "--limit", "-l", type=float, help="Limit czasu odpowiedzi", default=10
)
parser.add_argument("--czas", "-c", type=float, help="Limit czasu gry")
parser.add_argument("--goal", "-g", type=int, help="Cel punktów")
parser.add_argument(
    "--minimum_x", "-mnx", type=int, help="Minimalna wartość liczby nr1", default=2
)
parser.add_argument(
    "--minimum_y", "-mny", type=int, help="Minimalna wartość liczby nr2", default=2
)
parser.add_argument(
    "-maximum_x", "-mxx", type=int, help="Maksymalna wartość liczby nr1", default=9
)
parser.add_argument(
    "-maximum_y", "-mxy", type=int, help="Maksymalna wartość liczby nr2", default=9
)

args = parser.parse_args()

print("Hint: 0 to quit")
begin = datetime.now()
score = 0
goal = args.goal

while True:
    x = random.randint(args.minimum_x, args.maximum_x)
    y = random.randint(args.minimum_y, args.maximum_y)

    start = time.time()
    z = pobierz(f"{x} x {y} = ")

    if z == 0:
        break
    end = time.time()

    if x * y == z:
        score = score + 2
        print("dobrze")
        if end - start > args.limit:
            score = score - 1
            print(f"ale za długo ({end-start:.2f} sekund)")
    else:
        score = score - 1
        print(f"źle, powinno być", x * y)
        if end - start > args.limit:
            score = score - 1
            print(f"i za długo ({end-start:.2f} sekund)")
        while z != x * y:
            z = pobierz(f"Spróbuj jeszcze raz: {x} x {y} = ")
        print("OK")

    if args.czas is not None and datetime.now() > begin + timedelta(seconds=args.czas):
        print("Czas minał")
        break

    if args.goal is not None and score >= goal:
        print("Cel punktów został osiągniety")
        break

    podaj_wynik(score, args.czas is None)

print("Twój wynik to:", score, "punktów w czasie", datetime.now() - begin)
time.sleep(1)
