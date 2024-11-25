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
    z = int(input(f"ile to {x} razy {y}? "))
    if z == 0:
        q = int(input("Twój wynik to:", s "Punktów. Aby zakończyć wcisnij 0"))
        if q == 0:
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
