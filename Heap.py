capacity = 10

class Heap:
    def __init__(self):
        self.heap = [0] * capacity
        self.count = 0
    
    def insert(self, data):
        if capacity == self.count:
            print("Heap is full")
            return

        self.heap[self.count] = data
        self.count += 1

        self.heapify_up(self.count - 1)

    def heapify_up(self, index):
        parent_index = (index-1)//2
        if index>0 and self.heap[parent_index] < self.heap[index]:
            self.swap(parent_index, index)
            self.heapify_up(parent_index)

    def swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def get_max(self):
        return self.heap[0]

    def poll(self):
        max = self.get_max()

        self.swap(0, self.count-1)
        self.count -= 1
        self.heapify_down(0)
        return max

    def heapify_down(self, index):
        index_left = 2 * index + 1
        index_right = index_left + 1
        index_largest = index

        if index_left < self.count and self.heap[index_left] > self.heap[index_largest]:
            index_largest = index_left

        if index_right < self.count and self.heap[index_right] > self.heap[index_largest]:
            index_largest = index_right

        if index != index_largest:
            self.swap(index_largest, index)
            self.heapify_down(index_largest)


    def heap_sort(self):
        for i in range(self.count):
            print(self.poll())


heap = Heap()
heap.insert(10)
heap.insert(5)
heap.insert(8)
heap.insert(20)
# print(heap.poll())
# print(heap.poll())
heap.heap_sort()


