def bubble_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


n = int(input("Enter no. of elements: "))

arr = []

print("Enter the elements:")

for i in range(n):
    arr.append(int(input()))

bubble_sort(arr)

print("Sorted Array:")

for element in arr:
    print(element, end=" ")
