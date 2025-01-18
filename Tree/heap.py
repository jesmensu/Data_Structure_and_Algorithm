
class Heap:
    def __init__(self):
        self.heap = []
        self.size = 0

    def pos_parent(self, pos):
        return ((pos-1)//2)
    def pos_lChild(self, pos):
        return 2 * pos + 1
    def pos_rChild(self, pos):
        return ((2 * pos) + 2)
    def isLeaf(self, pos):
        return pos*2 + 1 > self.size
    def swap(self, fpos, spos):
        self.heap[fpos], self.heap[spos] = self.heap[spos], self.heap[fpos]

    def insert_item(self, data):
        # bottom up approch
        self.heap.append(data)
        self.size += 1
        pos = self.size -1
        while(pos!=0):
            p_pos = self.pos_parent(pos)
            if self.heap[pos] < self.heap[p_pos]:
                self.swap(pos, p_pos)
                pos = p_pos
            else:
                break

    def heapify(self, pos):
        # Top down approch. Every element will heapify through top down approach.
        largest_pos = pos
        lchild_pos = self.pos_lChild(pos)
        rchild_pos = self.pos_rChild(pos)
        if lchild_pos<self.size and self.heap[largest_pos] < self.heap[lchild_pos]:
            largest_pos = lchild_pos
        if rchild_pos<self.size and self.heap[largest_pos] < self.heap[rchild_pos]:
            largest_pos = rchild_pos  
        if largest_pos != pos:
            self.swap(pos, largest_pos)
            self.heapify(largest_pos)


    def remove(self):
        if self.size <= 0:
            raise IndexError("Sequence out of range")
        self.swap(0, self.size-1)
        self.size -= 1
        item = self.heap.pop()
        self.heapify(0)
        return item

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

