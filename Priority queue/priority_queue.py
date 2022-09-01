class Heap:
    def __init__(self, A):
        self.heap = A
        self.heap_size = len(A)
        for i in range(self.heap_size//2-1, -1, -1):
            self._max_heapify(i)

    def __str__(self):
        return str(self.heap)

    def __iter__(self):
        return self.heap.__iter__()

    def parent(self, i):
        return (i + 1) // 2 - 1

    def left(self, i):
        return 2*(i + 1) - 1

    def right(self, i):
        return 2*(i + 1)

    def heap_maximum(self):
        return self.heap[0]

    def _max_heapify(self, i):
        l = self.left(i)
        r = self.right(i)
        if l <= self.heap_size-1 and self.heap[l] > self.heap[i]:
            largest = l
        else:
            largest = i
        if r <= self.heap_size-1 and self.heap[r] > self.heap[largest]:
            largest = r
        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self._max_heapify(largest)

    def heap_extract_max(self):
        if self.heap_size < 1:
            raise 'The queue is empty'
        maximum = self.heap[0]
        self.heap[0] = self.heap[self.heap_size-1]
        self.heap_size -= 1
        self.heap.pop()
        self._max_heapify(0)
        return maximum

    def _heap_increase_key(self, i, key):
        if key < self.heap[i]:
            raise 'The new key is smaller than the current one'
        while i > 0 and self.heap[self.parent(i)] < key:
            self.heap[i] = self.heap[self.parent(i)]
            i = self.parent(i)
        self.heap[i] = key

    def max_heap_insert(self, key):
        self.heap_size += 1
        self.heap.append(key-1)
        self._heap_increase_key(self.heap_size-1, key)

    def heap_delete(self, i):
        if 0 <= i < self.heap_size:
            self.heap.pop(i)
            self.heap_size -= 1
            self._max_heapify(i)


def main():
    heap = Heap([17, 27, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0])
    print(heap)
    heap.max_heap_insert(30)
    print(heap)
    m = heap.heap_extract_max()
    print(m, heap)
    heap.heap_delete(6)
    print(heap)


if __name__ == '__main__':
    main()
