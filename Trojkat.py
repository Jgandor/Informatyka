def sprawdz(a, b, c):
    return a + b >= c and b + c >= a and a + c >= b


def sprawdz2(a, b, c):
    if a + b <= c:
        return False
    if b + c <= a:
        return False
    if a + c <= b:
        return False
    return True


a = int(input("Podaj bok a: "))
b = int(input("Podaj bok b: "))
c = int(input("Podaj bok c: "))

if sprawdz2(a, b, c):
    print("To jest trójkąt")
else:
    print("To NIE jest trójkąt")
