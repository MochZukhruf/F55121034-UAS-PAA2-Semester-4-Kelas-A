import time

def bubble_sort(arr):
    n = len(arr)
    start_time = time.time()
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    end_time = time.time()
    return arr, end_time - start_time

def insertion_sort(arr):
    n = len(arr)
    start_time = time.time()
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    end_time = time.time()
    return arr, end_time - start_time

def print_iterations(arr, method):
    n = len(arr)
    iterations = min(5, n)
    print("5 Iterasi Pertama Dan Terakhir:")
    for i in range(iterations):
        print(arr[i], end=" ")
    print("... ", end="")
    for i in range(n - iterations, n):
        print(arr[i], end=" ")
    print()
    print()

def print_time_elapsed(time_elapsed):
    print("Waktu komputasi:", round(time_elapsed, 6), "detik")
    print()

def analyze_algorithm():
    arr = [12, 99, 62, 15, 20, 95, 39, 48, 3, 24, 8, 43, 74, 19, 97, 33, 49, 68, 55, 33, 90, 90, 7,
           26, 85, 46, 39, 40, 9, 36, 60, 64, 89, 31, 25, 71, 21, 23, 63, 84, 32, 5, 3, 44, 21, 10, 21,
           17, 50, 2, 36, 53, 79, 54, 19, 88, 1, 32, 31, 15, 6, 3, 1, 40, 22, 43, 18, 1, 77, 9, 59,
           40, 7, 41, 81]

    while True:
        print("Algoritma yang tersedia:")
        print("1. Bubble Sort")
        print("2. Insertion Sort")
        print("3. Keluar")
        choice = int(input("Pilih: "))

        if choice == 1:
            print("Bubble Sort")
            print("Sebelum:", arr)
            sorted_arr, time_elapsed = bubble_sort(arr.copy())
            print_iterations(sorted_arr, "Bubble Sort")
            print("Sesudah:", sorted_arr)
            print_time_elapsed(time_elapsed)
        elif choice == 2:
            print("Insertion Sort")
            print("Sebelum:", arr)
            sorted_arr, time_elapsed = insertion_sort(arr.copy())
            print_iterations(sorted_arr, "Insertion Sort")
            print("Sesudah:", sorted_arr)
            print_time_elapsed(time_elapsed)
        elif choice == 3:
            break
        else:
            print("Mohon Pilih Kembali.")

analyze_algorithm()
