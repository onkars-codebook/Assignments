import random
import timeit

arr = [random.randint(1, 1000000) for _ in range(100000)]
print(' Array Size:', len(arr))

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + mid + quick_sort(right)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    res = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    res.extend(left[i:])
    res.extend(right[j:])
    return res


def run_quick():
    quick_sort(arr.copy())

def run_merge():
    merge_sort(arr.copy())


quick_t = timeit.timeit(run_quick, number=1)
merge_t = timeit.timeit(run_merge, number=1)

print(f"Quick Sort Time: {quick_t:.2f} sec")
print(f"Merge Sort Time: {merge_t:.2f} sec")
