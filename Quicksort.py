def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]

    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)


# User input
arr = list(map(int, input("Enter numbers separated by spaces: ").split()))

print("Original array:", arr)

sorted_arr = quick_sort(arr)

print("Sorted array:", sorted_arr)
