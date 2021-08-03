def RLEncode(arr) :
    retArr = []
    tempItem = arr[0]
    count = 0

    for item in arr :
        if item != tempItem :
            if count == 1 :
                retArr.append(tempItem)
            else :
                retArr.append([count, tempItem])

            count = 1
            tempItem = item
        else :
            count += 1

    retArr.append([count, tempItem])

    return retArr

if __name__ == '__main__' :
    arr = ['A', 'A', 'A', 'A', 'B', 'C', 'C', 'A', 'A', 'D', 'E', 'E', 'E', 'E']

    print("The original List : ", arr)

    arr = RLEncode(arr)

    print("List after Run-Length Encoding : ", arr)