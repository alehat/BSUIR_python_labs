def quick_sort(array):
    return quick_sort([x for x in array[1:] if x < array[0]]) + [array[0]] + \
           quick_sort([x for x in array[1:] if x >= array[0]]) if len(array) > 1 else array


def merge_sort(array):
    if len(array) < 2:
        return array

    mid = len(array) // 2
    result = []

    sub_arr1 = merge_sort(array[:mid])
    sub_arr2 = merge_sort(array[mid:])

    while (len(sub_arr1) > 0) and (len(sub_arr2) > 0):
        if sub_arr1[0] > sub_arr2[0]:
            result.append(sub_arr2.pop(0))
        else:
            result.append(sub_arr1.pop(0))

    result.extend(sub_arr2 + sub_arr1)
    return result


def radix_sort(array):
    max_len = -1
    for number in array:
        num_len = len(str(number))
        if num_len > max_len:
            max_len = num_len
    buckets = [[] for _ in range(0, 10)]
    for digit in range(0, max_len):
        for number in array:
            buckets[number / 10**digit % 10].append(number)
        del array[:]
        for bucket in buckets:
            array.extend(bucket)
            del bucket[:]
    return array


def sorts(algo):
    line = raw_input('Input numbers: \n')
    numbers = [int(x) for x in line.split()]
    if algo == 'qsort':
        return quick_sort(numbers)

    if algo == 'merge':
        return merge_sort(numbers)

    if algo == 'radix':
        return radix_sort(numbers)
