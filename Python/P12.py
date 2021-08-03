def RLDecode(arr) :
    '''
    Used to decode the Run-Length encoded list.

    Parameters :
        arr (List) : Run-Length Encoded list.

    Returns :
        decodedArr (List) : Run-Length Decoded to plain 1D List.

    Example :
        For List [[4, 'A'], 'B', [2, 'C'], [2, 'A'], 'D', [4, 'E']]
        Returns new list ['A', 'A', 'A', 'A', 'B', 'C', 'C', 'A', 'A', 'D', 'E', 'E', 'E', 'E']
    '''

    decodedArr = []

    # Iterate over given.
    for item in arr :

        # If the given element is list itself,
        if isinstance(item, list) :
            # Append the element to it's frequency times
            for i in range(item[0]) :
                decodedArr.append(item[1])
        else :
            decodedArr.append(item)

    return decodedArr


if __name__ == '__main__':
    arr = [[4, 'A'], 'B', [2, 'C'], [2, 'A'], 'D', [4, 'E']]

    print("The Run-Length Encoded array is : ", arr)

    arr = RLDecode(arr)

    print("Array after Decoding : ", arr)