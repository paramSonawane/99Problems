def lsort(arr) :
    '''
    Sort given multidiamensional list according to length of it's sublist.

    Parameters :
        arr (List) : Array which is to be sorted.

    Returns :
        arr (List) : Sorted array according to length of the sublist.
    '''
    length = len(arr)

    # Use bubble sort with length of the substring as comparator.
    for i in range(length - 1) :
        for j in range(0, length - i - 1) :
            if len(arr[j]) > len(arr[j + 1]) :
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr
    

if __name__ == '__main__' :
    arr = [['a', 'b', 'c'], ['d', 'e'], ['f', 'g', 'h'], ['d', 'e'], ['i', 'j', 'k', 'l'], ['m', 'n'], ['o']]

    print("Array before sorting : ", arr)

    lsort(arr)

    print("Array After sorting : ", arr)