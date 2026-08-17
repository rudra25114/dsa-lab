def search(emp_list, x, i=0):
    if i == len(emp_list):
        return False

    if emp_list[i] == x:
        return True

    return search(emp_list, x, i + 1)


emp_list = [101, 205, 310, 415, 520]

x = int(input("Enter employee ID to search: "))

if search(emp_list, x):
    print("Employee ID found.")
else:
    print("Employee ID not found.")
