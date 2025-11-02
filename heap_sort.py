import max_heap

def heap_sort(A):
    sorted_A = [None] * len(A)
    A = max_heap.maxHeap(A)
    for i in range(A.heap_size-1,-1,-1):
        sorted_A[i] = A.heap_extract_max()
    return sorted_A

A = [100,1,20,50,2,51,200,600,300,12,42,6,53,42,7,54]
print(heap_sort(A))
