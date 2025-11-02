def quickSort(A,p,r):
    if p < r:
        split = partition(A,p,r)
        quickSort(A,p,split-1)
        quickSort(A,split+1,r)

def partition(A,p,r):
    pivot = A[r]
    i = p - 1
    for j in range(p,r):
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1

A=[1,2,77,33,11,86,100,200,150]
quickSort(A,0,len(A)-1)
print(A)
