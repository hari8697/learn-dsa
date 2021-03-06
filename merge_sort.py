def merge_sort(list):
    """
    Returns a new sorted list in ascending order

    Takes O(n log n) time
    Takes O(n) space
    """

    if len(list) <= 1:
        return list

    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)


def split(list):
    """
    Divide the unsorted list into sublists
    Returns two sublists - left and right

    Takes 0(k log n) time 
    with split func of python, since split takes O(k) time

    In regular constant time search and split like in iterative binary ssearch, this takes O(log n) time
    """

    mid = len(list)//2
    left = list[:mid]
    right = list[mid:]

    return left, right


def merge(left, right):
    """
    Merges 2 lists/arrays, sorting them in the process
    Returns new merged list

    Runs in overall O(n) time
    """

    l = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if(left[i] < right[j]):
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1

    while i < len(left):
        l.append(left[i])
        i += 1

    while j < len(right):
        l.append(right[j])
        j += 1

    return l


alist = [12, 23, 1, 13, 4, 5, 7, 8, 2, 9]


def verify_sorted(list):
    n = len(list)

    if n == 0 or n == 1:
        return True

    return list[0] < list[1] and verify_sorted(list[1:])


print(verify_sorted(alist))

l = merge_sort(alist)
print(l)
print(verify_sorted(l))
