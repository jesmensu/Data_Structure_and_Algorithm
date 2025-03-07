import math

class SegmentTree:
    def __init__(self, arr):
        self.arr = arr
        self.size_arr = len(arr)
        self.tree = [math.inf] * (4*self.size_arr)

    def build(self, node, start, end):
        if start == end:
            self.tree[node] = self.arr[start]
        else:
            mid = (start + end) // 2
            l_child = 2*node + 1
            r_child = 2*node + 2
            self.build(l_child, start, mid)
            self.build(r_child, mid+1, end)
            self.tree[node] = min(self.tree[l_child], self.tree[r_child])

    def query(self, node, start, end, l_index, r_index):
        # Outside the range
        if r_index < start or l_index > end:
            return math.inf
        
        # complete overlap
        if l_index <= start and end <= r_index:
            return self.tree[node]
        
        # Partial overlap
        mid = (start + end) // 2
        l_child = 2*node + 1
        r_child = 2*node + 2
        l_result = self.query(l_child, start, mid, l_index, r_index)
        r_result = self.query(r_child, mid+1, end, l_index, r_index)

        return min(l_result, r_result)
    


arr = [1, 3, -1, 7, 2, 11]
st = SegmentTree([1, 3, -1, 7, 2, 11])
st.build(0,0,len(arr)-1)
print(st.tree)
print(st.query(0,0, len(arr)-1, 3,5))

