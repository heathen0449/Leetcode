# 堆--其实就是一个数组
# 可以近似看作一个完全二叉树，树[0]是根节点，树[i]的左子节点是树[2*i]，右子节点是树[2*i+1]
# 一个节点的父节点是树(i//2)(向下取整)
# 上述写法是算法导论中，数据以1为起始索引，这里以0为起始索引
# 一个节点的左子节点是2*i+1，右子节点是2*i+2，父节点是(i-1)//2

# 这里需要heapsize是因为堆排序的时候，堆的大小会变化，所以需要一个变量来记录堆的大小
# index是默认的根结点，代表着以应该为最大值的索引的位置
# max_heapify是维护堆的性质，即根结点的值大于左右子节点的值


# 维护最大堆性质
def max_heapify(arr, index, heap_size):
    left = 2 * index + 1
    right = 2 * index + 2

    if left < heap_size and arr[left] > arr[index]:
        largest = left
    else:
        largest = index
    
    if right < heap_size and arr[right] > arr[largest]: 
        largest = right
    
    if largest != index:
        arr[index], arr[largest] = arr[largest], arr[index]
        max_heapify(arr, largest, heap_size)


# 建堆,请记住性质，叶子结点的范围是[(len-1)//2 + 1, heap_size-1]

def build_heap(arr):
    heap_size = len(arr)
    for i in range((len(arr)-1)//2, -1, -1):
        max_heapify(arr, i, heap_size)

def heap_sort(arr):
    # 先建立大根堆
    build_heap(arr)
    for i in range(len(arr) - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        max_heapify(arr, 0, i)

def topK(arr, k):
    build_heap(arr)
    # 因为是找第k大的数，并且构建最大堆的时候已经找到第一大的数了，所以只执之行k-1次，
    for i in range(1,k):
        arr[0], arr[len(arr) - i] = arr[len(arr) - i], arr[0]
        max_heapify(arr, 0, len(arr) - i)
    return arr[0]

arr = [6,3,1,4,2,5]
print(topK(arr,2))
heap_sort(arr)
print(arr)


