def RLEncode(arr) :
    '''
    Used to print the Run-Length Encoded version of List.

    Parameter :
        arr (List) : List of elements with some repeating values.

    Returns :
        retArr (List) : Run-Length encoded list.

    Example :
        If the list is (1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 5, 5, 5)
        It will print (1X2, 2X3, 3X4, 4X1, 5X3)
    '''

    retArr = []
    tempItem = arr[0]
    count = 0

    # Iterate over list, each time keeping track of frequency of element.
    for item in arr :
        if item != tempItem :
            # Append the previous element and its count to retArr.
            
            if count == 1 :
                retArr.append(tempItem)
            else :
                retArr.append([count, tempItem])

            count = 1
            tempItem = item
        else :
            # Keep incrementing the count till new element is found.
            count += 1

    retArr.append([count, tempItem])

    return retArr

if __name__ == '__main__' :
    arr = ['A', 'A', 'A', 'A', 'B', 'C', 'C', 'A', 'A', 'D', 'E', 'E', 'E', 'E']

    print("The original List : ", arr)

    arr = RLEncode(arr)

    print("List after Run-Length Encoding : ", arr)