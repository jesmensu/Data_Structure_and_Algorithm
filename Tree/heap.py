
class Heap:
    def __init__(self):
        self.heap = []
        self.size = 0

    def pos_parent(self, pos):
        return ((pos-1)//2)
    def pos_lChild(self, pos):
        return 2 * pos + 1
    def pos_rChild(self, pos):
        return (2 * pos) + 2
    def isLeaf(self, pos):
        return pos*2 + 1 > self.size
    def swap(self, fpos, spos):
        self.Heap[fpos], self.Heap[spos] = self.Heap[spos], self.Heap[fpos]

    def insert_item(self, data):
        self.heap.append(data)
        self.size += 1
        current = self.size -1
        while(self.heap[current] > self.heap[(current-1)//2] and current>=0):
            self.heap[current], self.heap[(current-1)//2] = self.heap[(current-1)//2], self.heap[current]
            current = (current-1)//2

    def heapify(self, pos):
        if self.size > self.pos_rChild(pos):
            if self.heap[pos] < self.heap[self.pos_lChild(pos)] or self.heap[pos] < self.heap[self.pos_rChild(pos)]:
                if self.heap[self.pos_lChild(pos)] > self.heap[self.pos_rChild(pos)]:
                    self.heap[pos], self.heap[self.pos_lChild(pos)] = self.heap[self.pos_lChild(pos)], self.heap[pos]
                    self.heapify(self.pos_lChild(pos))
                else:
                    self.heap[pos], self.heap[self.pos_rChild(pos)] = self.heap[self.pos_rChild(pos)], self.heap[pos]
                    self.heapify(2*pos+2)
        
        elif self.size > self.pos_lChild(pos):
            if self.heap[pos] < self.heap[self.pos_lChild(pos)]:
                self.heap[pos], self.heap[self.pos_lChild(pos)] = self.heap[self.pos_lChild(pos)], self.heap[pos]

    def remove(self):
        self.heap[0] = self.heap[self.size-1]
        self.heap.pop(-1)
        self.size -= 1
        self.heapify(0)

    def heapify_list(self, lst):
        self.heap = lst
        self.size = len(lst)
        if self.heap:
            for i in range(int((self.size-1)/2), -1, -1):
                self.heapify(i)

    def is_max_heap(self):
        heap = self.heap
        if heap:
            for i in range(int((self.size-1)/2)):
                if heap[i]< heap[2*i + 1] or heap[i]< heap[2*i + 2]:
                    return False
            else:
                return True

    

h = Heap()
# h.insert_item(70)
# h.insert_item(60)
# h.insert_item(43)
# h.insert_item(25)
# h.insert_item(80)
# h.insert_item(40)
# h.insert_item(100)
# h.insert_item(90)
# h.heapify(0)
lst = [30,70,60,100,40,45,50,95,30]
h.heapify_list(lst)
print(h.is_max_heap())
print(h.heap)
h.remove()
print(h.heap)
print(h.is_max_heap())

