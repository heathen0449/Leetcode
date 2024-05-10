# 快速排序的核心思想是分治法，每次选取一个主元，将数组分为两部分，左边的元素小于主元，右边的元素大于主元

# start: 开始位置 pivot: 主元位置
# 返回主元位置元素应有的位置
def partition(arr, start, pivot):
    key = arr[pivot]
    i, j = start - 1, start
    # [p..i] arr[] < arr[pivot]
    # [i+1..j] arr[] >= arr[pivot]
    # [j+1.. pivot] 未知
    for j in range(start, pivot):
        # 找到比主元小的值，将较大的值挪到前方
        if arr[j] < key:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
        
    # 最终找到应有位置i+1，交换并返回索引

    arr[i+1], arr[pivot] = arr[pivot], arr[i+1]
    return i + 1

def quick_sort(arr, start, pivot):
    if start >= pivot:
        return 
    new_p = partition(arr, 0, pivot)
    quick_sort(arr, start, new_p-1)
    quick_sort(arr, new_p + 1, pivot)

array = [5, 2, 4, 6, 1, 3]
quick_sort(array, 0, len(array)-1)
print(array)
