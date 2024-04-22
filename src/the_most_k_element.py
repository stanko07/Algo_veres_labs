def partition(array, lower, upper):
    mid = (lower + upper) // 2
    pivot = array[mid]
    while lower <= upper:
        while array[lower] < pivot:
            lower += 1
        while array[upper] > pivot:
            upper -= 1
        if lower <= upper:
            array[lower], array[upper] = array[upper], array[lower]
            lower += 1
            upper -= 1
    return lower


def quickSort(array, lower, upper):
    if lower < upper:
        index = partition(array, lower, upper)
        quickSort(array, lower, index - 1)
        quickSort(array, index, upper)


def search_the_largest_k(arr, k):
    if k > len(arr) or len(arr) is None:
        return None
    else:
        original_arr = list(arr)
        quickSort(arr, 0, len(arr) - 1)
        element = arr[-k]
        position = original_arr.index(element)
        return element  ,  position
