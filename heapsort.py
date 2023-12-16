class Heap:
    def __init__(self):
        self.heap = []

    def heapify(self, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and self.heap[left] > self.heap[largest]:
            largest = left

        if right < n and self.heap[right] > self.heap[largest]:
            largest = right

        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.heapify(n, largest)

    def build_heap(self, arr):
        n = len(arr)
        self.heap = arr
        for i in range(n//2, -1, -1):
            self.heapify(n, i)

    def increase_key(self, i, key):
        self.heap[i] = key
        while i > 0 and self.heap[i//2] < self.heap[i]:
            self.heap[i//2], self.heap[i] = self.heap[i], self.heap[i//2]
            i = i//2

    def heap_insert(self, key):
        self.heap += [float('-inf')]
        self.increase_key(len(self.heap) - 1, key)

    def heap_delete(self, i):
        self.heap[i] = self.heap[-1]
        del self.heap[-1]
        self.heapify(len(self.heap), i)

def main():
    heap = Heap()

    # Construindo um heap a partir de uma lista
    arr = [9, 4, 7, 1, 8, 5]
    heap.build_heap(arr)

    print("Heap original:")
    print(heap.heap)
    heap.heap_insert(10)
    print("Heap após inserir elemento:")
    print(heap.heap)
    heap.heap_delete(2)
    print("Heap após deletar elemento na posição 2:")
    print(heap.heap)

if __name__ == "__main__":
    main()