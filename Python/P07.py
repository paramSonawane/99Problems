flatArr = []

def flatten(arr) :
    '''
    This function will flatten the given array to a single 1D array.

    Parameters :
        arr (List) : Multi diamentional array to be flattened.

    Returns :
        flatArr (List) : Flat 1D list extracted from arr.

    Example :
        List [1, [2, [3, 4], 5]] will be converted to
        [1, 2, 3, 4, 5] and returend.
    '''

    # Recurse until single element is found.
    for item in arr :
        if isinstance(item, list) :
            for subItem in item :
                flatten(subItem)

        # Base condition for recursion.
        else :
            flatArr.append(item)

    return flatArr

if __name__ == '__main__' :
    arr = ['a', ['b', ['c', 'd'], 'e']]

    print("The given array is : ", arr)

    arr = flatten(arr)

    print("The flattened array is : ", arr)