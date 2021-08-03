def lsort(arr) :
    length = len(arr)

    for i in range(length - 1) :
        for j in range(0, length - i - 1) :
            if len(arr[j]) > len(arr[j + 1]) :
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

if __name__ == '__main__' :
    arr = [['a', 'b', 'c'], ['d', 'e'], ['f', 'g', 'h'], ['d', 'e'], ['i', 'j', 'k', 'l'], ['m', 'n'], ['o']]

    print("Array before sorting : ", arr)

    lsort(arr)

    print("Array After sorting : ", arr)