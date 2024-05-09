def merge(arr: list[int], start, mid, end):
    left= arr[start:mid+1]
    right = arr[mid+1:end+1]
    i, j = 0, 0
    key = start
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[key] = left[i]
            i += 1
        else:
            arr[key] = right[j]
            j += 1
        key += 1 

    if i < len(left):
        arr[key:end+1] = left[i:]
    if j < len(right):
        arr[key:end+1] = right[j:]


def merge_sort(arr: list[int], start: int, end: int) -> None:
    if start >= end:
        return
    mid = (start + end) // 2
    merge_sort(arr, start, mid)
    merge_sort(arr, mid+1, end)
    merge(arr, start, mid, end)

arr = [5, 2, 4, 6, 1, 3]
merge_sort(arr, 0, len(arr)-1)
print(arr)