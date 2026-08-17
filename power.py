def power(p, n):
    if n == 0:
        return 1
    elif n < 0:
        return 1 / power(p, -n)
    else:
        return p * power(p, n - 1)

p = float(input("Enter the principal growth factor: "))
n = int(input("Enter the number of years: "))

print("Power =", power(p, n))
