def countdown(n):
    if n == 0:
        print("launch")
    else:
        print(n)
        countdown(n - 1)

n = int(input("Enter the starting number: "))
countdown(n)
