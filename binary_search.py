def binary_search(list, target):
    first = 0
    last = len(list) - 1

    while(first <= last):
        middle = (first + last) // 2

        if(list[middle] == target):
            return middle
        elif(list[middle] < target):
            first = middle + 1
        else:
            last = middle - 1
    return -1


list = [1, 2, 3, 4, 5, 6, 7, 8]


def verify(result):
    print('Target exists at:', result)



result = binary_search(list, 0)
verify(result)

result = binary_search(list, 8)
verify(result)

result = binary_search(list, 1)
verify(result)

result = binary_search(list, 12)
verify(result)
