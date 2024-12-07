def czy_rosnie(x):
    for i in range(len(x) - 1):
        d = x[i] - x[i + 1]
        if d <= -4 or d >= 0:
            return False
    return True

def czy_maleje(x):
    for i in range(len(x) - 1):
        d = x[i] - x[i + 1]
        if d <= 0 or d >= 4:
            return False
    return True

def sprawdz(x):
    return czy_rosnie(x) or czy_maleje(x)

xx =[
    [7, 6, 4, 2, 1],
    [1, 2, 7, 8, 9],
    [9, 7, 6, 2, 1],
    [1, 3, 2, 4, 5],
    [8, 6, 4, 4, 1],
    [1, 3, 6, 7, 9],
]

liczba = 0
for x in xx:
    if sprawdz(x):
        liczba += 1
print(liczba)

liczba = 0
with open("Adventofcode2.txt") as plik:
    for linia in plik:
        x  = [int(s) for s in linia.split()]
        print(x, sprawdz(x))
        if sprawdz(x):
            liczba += 1
print(liczba) 
