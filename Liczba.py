import random
import time
import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    "--limit", "-l", type=float, help="Limit czasu odpowiedzi", default=10
)
args = parser.parse_args()
print("Hint: 0 to quit")
s = 0
while True:
    x = random.randint(2, 9)
    y = random.randint(2, 9)
    start = time.time()
    z = int(input(f"{x} x {y} = ? "))
    if z == 0:
        print("Twój wynik to:", s, "punktów")
        time.sleep(3)
        exit()
    end = time.time()
    if x * y == z:
        s = s + 2
        print("dobrze")
        if end - start > args.limit:
            s = s - 1
            print(f"ale za długo ({end-start:.2f} sekund)")
    else:
        s = s - 1
        print(f"źle, powinno być", x * y)
        if end - start > args.limit:
            s = s - 1
            print(f"i za długo ({end-start:.2f} sekund)")
        while z != x * y:
            z = int(input("Spróbuj jeszcze raz: "))
        print("Dobrze")
    print("Masz", s, "punktów, przygotuj się", end=' ', flush=True)
    for i in range(3):
        print('.', end=' ', flush=True)
        time.sleep(1)
    print()
