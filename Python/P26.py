# Generate the combinations of K distinct objects chosen from the N elements of a list.

if __name__ == '__main__' :
    arr = []

    for i in range(0, 12) :
        arr.append(i)

    for i in range(2,9) :
        print("(", end="")

        for j in range(1,10) :
            print("(", end="")

            for k in range(0,11) :
                print("( {}, {}, {}),".format(arr[i], arr[j], arr[k]), end="")

            print("),")

        print(")")
