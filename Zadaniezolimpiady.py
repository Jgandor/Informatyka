Total = 0
for a in range(1, 10):
    for b in range(10):
        for c in range(10):
            for d in range(1, 10):
                suma = a * 1000 + b * 100 + c * 10 + d
                if suma - (1000 * d + 100 * c + 10 * b + a) == 2997:
                    Total += 1
                    print(Total, suma)
