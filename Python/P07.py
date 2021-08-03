flatArr = []

def flatten(arr) :
    for item in arr :
        if isinstance(item, list) :
            for subItem in item :
                flatten(subItem)
        else :
            flatArr.append(item)

    return flatArr

if __name__ == '__main__' :
    arr = ['a', ['b', ['c', 'd'], 'e']]

    print("The given array is : ", arr)

    arr = flatten(arr)

    print("The flattened array is : ", arr)