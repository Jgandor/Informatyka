import random
import time

LIMIT = 7

while True:
    x = random.randint(2, 9)
    y = random.randint(2, 9)
    start = time.time()
    z=int(input(f"ile to {x} razy {y}? "))
    end = time.time()
    if x * y == z:
        print("dobrze")
        if end - start > LIMIT:
            print(f"ale za długo ({end-start:.2f} sekund)")
    else:
        print(f"źle, powinno być", x*y)
        if end - start > LIMIT:
            print(f"i za długo ({end-start:.2f} sekund)")
