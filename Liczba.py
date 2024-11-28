import argparse
import datetime
import random
import time


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
args = parser.parse_args()

print("Hint: 0 to quit")
begin = datetime.datetime.now()
score = 0
goal = args.goal

while True:
    x = random.randint(2, 9)
    y = random.randint(2, 9)

    start = time.time()
    z = int(input(f"{x} x {y} = ? "))
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
            z = int(input("Spróbuj jeszcze raz: "))
        print("Dobrze")
    if args.czas is not None and datetime.datetime.now() > begin + datetime.timedelta(
        seconds=args.czas
    ):
        print("Czas minał")
        break
    if args.goal is not None and score >= goal:
        print("Cel punktów został osiągniety")
        break
    podaj_wynik(score, args.czas is None)

print("Twój wynik to:", score, "punktów w czasie", datetime.datetime.now() - begin)
time.sleep(1)
