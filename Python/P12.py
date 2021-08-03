def RLDecode(arr) :
    decodedArr = []
    for item in arr :
        if isinstance(item, list) :
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