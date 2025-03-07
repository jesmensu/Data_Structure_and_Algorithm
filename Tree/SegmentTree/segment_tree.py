class SegmentTree:
    def __init__(self, arr, operation, neutral_value):
        """
        Initializes the segment tree.

        :param arr: Input array to build the segment tree from.
        :param operation: A function representing the operation (e.g., sum, min, max, gcd).
        :param neutral_value: A value that doesn't affect the operation (e.g., 0 for sum, infinity for min).
        """
        self.n = len(arr)
        self.tree = [neutral_value] * (4 * self.n)
        self.operation = operation
        self.neutral_value = neutral_value
        self.build(arr, 0, 0, self.n - 1)

    def build(self, arr, node, start, end):
        """
        Recursively builds the segment tree.

        :param arr: Input array.
        :param node: Current node index in the segment tree.
        :param start: Start index of the segment.
        :param end: End index of the segment.
        """
        if start == end:
            # Leaf node: store the value of the array
            self.tree[node] = arr[start]
        else:
            # Internal node: recursively build left and right children
            mid = (start + end) // 2
            left_child = 2 * node + 1
            right_child = 2 * node + 2

            self.build(arr, left_child, start, mid)
            self.build(arr, right_child, mid + 1, end)

            # Combine results from left and right children
            self.tree[node] = self.operation(self.tree[left_child], self.tree[right_child])

    def query(self, node, start, end, l, r):
        """
        Queries the segment tree for the result in range [l, r].

        :param node: Current node index in the segment tree.
        :param start: Start index of the segment represented by the current node.
        :param end: End index of the segment represented by the current node.
        :param l: Left index of the query range.
        :param r: Right index of the query range.
        :return: Result of the operation in the range [l, r].
        """
        if r < start or l > end:
            # Completely outside the range
            return self.neutral_value

        if l <= start and end <= r:
            # Completely inside the range
            return self.tree[node]

        # Partially inside and partially outside
        mid = (start + end) // 2
        left_child = 2 * node + 1
        right_child = 2 * node + 2

        left_result = self.query(left_child, start, mid, l, r)
        right_result = self.query(right_child, mid + 1, end, l, r)

        return self.operation(left_result, right_result)

    def update(self, node, start, end, idx, value):
        """
        Updates the value at index `idx` in the array.

        :param node: Current node index in the segment tree.
        :param start: Start index of the segment represented by the current node.
        :param end: End index of the segment represented by the current node.
        :param idx: Index of the value to update.
        :param value: New value to update at index `idx`.
        """
        if start == end:
            # Leaf node: update the value
            self.tree[node] = value
        else:
            mid = (start + end) // 2
            left_child = 2 * node + 1
            right_child = 2 * node + 2

            if start <= idx <= mid:
                # Update left child
                self.update(left_child, start, mid, idx, value)
            else:
                # Update right child
                self.update(right_child, mid + 1, end, idx, value)

            # Recalculate current node value
            self.tree[node] = self.operation(self.tree[left_child], self.tree[right_child])

    def range_query(self, l, r):
        """
        Public method to query the range [l, r].
        """
        return self.query(0, 0, self.n - 1, l, r)

    def point_update(self, idx, value):
        """
        Public method to update the value at index `idx`.
        """
        self.update(0, 0, self.n - 1, idx, value)

if __name__ == "__main__":
    # Example array
    arr = [1, 3, 5, 7, 9, 11]

    # Create a segment tree for range sum queries
    seg_tree = SegmentTree(arr, operation=lambda x, y: x + y, neutral_value=0)

    # Perform range sum query for range [1, 3]
    print("Sum of range [1, 3]:", seg_tree.range_query(1, 3))  # Output: 15 (3 + 5 + 7)

    # Update the value at index 2 to 6
    seg_tree.point_update(2, 6)
    print("Updated array, new sum of range [1, 3]:", seg_tree.range_query(1, 3))  # Output: 16 (3 + 6 + 7)

    # Create a segment tree for range minimum queries
    seg_tree_min = SegmentTree(arr, operation=min, neutral_value=float("inf"))
    print("Minimum of range [1, 3]:", seg_tree_min.range_query(1, 3))  # Output: 3
