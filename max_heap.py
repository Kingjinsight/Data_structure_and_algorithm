class maxHeap():
    def __init__(self, A):
        self.A = A
        self.heap_size = len(A)
        self.build_max_heap()
    

    def build_max_heap(self):
        for i in range(int(self.heap_size/2)-1, -1, -1):
            self.max_heapify(i)
    
    def max_heapify(self, i):
        l = self.left(i)
        r = self.right(i)
        largest = i
        if l < self.heap_size and self.A[l] > self.A[i]:
            largest = l
        if r < self.heap_size and self.A[r] > self.A[largest]:
            largest = r
        if largest != i:
            self.A[i],self.A[largest] = self.A[largest],self.A[i]
            self.max_heapify(largest)

    def left(self, i):
        return i * 2 + 1
    
    def right(self, i):
        return i * 2 + 2
    
    def parent(self, i):
        if i == 0:
            return None
        return int(i/2+0.5) - 1
    
    def heap_extract_max(self):
        record = self.A[0]
        self.A[0] = self.A[self.heap_size-1]
        self.A.pop(self.heap_size-1)
        self.heap_size -= 1
        self.max_heapify(0)
        return record
    
    def max_heap_insert(self, k):
        self.heap_size += 1
        self.A.append(k)
        j = self.heap_size - 1
        while j != 0 and self.A[j] > self.A[self.parent(j)]:
            self.A[j], self.A[self.parent(j)] = self.A[self.parent(j)], self.A[j]
            j = self.parent(j)