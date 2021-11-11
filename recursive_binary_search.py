def recursive_binary_search(list, target):
    if len(list) == 0:
        return False
    else:
        midpoint = (len(list)) // 2

        if (list[midpoint] == target):
            return True
        else:
            if (list[midpoint] < target):
                return recursive_binary_search(list[midpoint+1:], target)
            else:
                return recursive_binary_search(list[:midpoint], target)



list = [1, 2, 3, 4, 5, 6, 7, 8]


def verify(result):
    print('Target exists:', result)


result = recursive_binary_search(list, 0)
verify(result)

result = recursive_binary_search(list, 8)
verify(result)

result = recursive_binary_search(list, 1)
verify(result)

result = recursive_binary_search(list, 12)
verify(result)
