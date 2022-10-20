class Value:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __repr__(self):
        return f'{__class__.__name__}({self.key}, {self.value})'


class PriorityQueue:
    def __init__(self, A=[]):
        self.heap = [Value(key, value) for key, value in A]
        self.size = len(A)
        for i in range(self.size//2-1, -1, -1):
            self._min_heapify(i)

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

    def heap_minimum(self):
        return self.heap[0].value

    def _min_heapify(self, i):
        left = self.left(i)
        right = self.right(i)
        if left <= self.size-1 and self.heap[left].key < self.heap[i].key:
            smallest = left
        else:
            smallest = i
        if right <= self.size-1 and self.heap[right].key < self.heap[smallest].key:
            smallest = right
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self._min_heapify(smallest)

    def extract_min(self):
        if self.size < 1:
            raise 'The queue is empty'
        minimum = self.heap[0].value
        self.heap[0] = self.heap[self.size-1]
        self.size -= 1
        self.heap.pop()
        self._min_heapify(0)
        return minimum

    def _heap_increase_key(self, i, val):
        if val.key < self.heap[i].key:
            raise 'The new key is larger than the current one'
        while i > 0 and self.heap[self.parent(i)].key > val.key:
            self.heap[i] = self.heap[self.parent(i)]
            i = self.parent(i)
        self.heap[i] = val

    def insert(self, key, value):
        self.size += 1
        val = Value(key, value)
        self.heap.append(val)
        self._heap_increase_key(self.size-1, val)

    def delete(self, i):
        if 0 <= i < self.size:
            self.heap.pop(i)
            self.size -= 1
            self._min_heapify(i)

    def replace_key(self, new_key, value):
        for i in range(self.size):
            if self.heap[i].value == value:
                self.heap[i].key = new_key
                self._heap_increase_key(i, self.heap[i])
                self._min_heapify(i)
                break
