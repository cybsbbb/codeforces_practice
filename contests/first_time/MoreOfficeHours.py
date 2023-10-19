import sys
input = sys.stdin.readline

def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))


class SegmentTree:
    def __init__(self, alist, merger_):
        self.data = alist[:]
        self._tree = [None] * 4 * len(self.data)
        self._merger = merger_

        self._buildSegmentTree(0, 0, len(self.data) - 1)

    def getSize(self):
        return len(self.data)

    def printSegmentTree(self):
        print(self._tree)

    def query(self, queryL, queryR):
        if queryL < 0 or queryR < 0 or queryL >= self.getSize() or queryR >= self.getSize() or queryR < queryL:
            raise Exception('Illegal query!')

        return self._query(0, 0, self.getSize()-1, queryL, queryR)

    def set(self, index, e):
        if index < 0 or index >= self.getSize():
            raise Exception('Illegal index!')
        self.data[index] = e
        self._set(0, 0, self.getSize()-1, index, e)

    def _leftChild(self, index):
        return 2 * index + 1

    def _rightChild(self, index):
        return 2 * index + 2

    def _buildSegmentTree(self, treeIndex, left, right):
        if left == right:
            self._tree[treeIndex] = self.data[left]
            return

        mid = left + (right - left) // 2
        leftChild_index = self._leftChild(treeIndex)
        rightChild_index = self._rightChild(treeIndex)

        self._buildSegmentTree(leftChild_index, left, mid)
        self._buildSegmentTree(rightChild_index, mid+1, right)
        self._tree[treeIndex] = self._merger(self._tree[leftChild_index], self._tree[rightChild_index])

    def _query(self, treeIndex, left, right, quaryL, quaryR):
        if left == quaryL and right == quaryR:
            return self._tree[treeIndex]

        mid = left + (right - left) // 2
        leftChild_index = self._leftChild(treeIndex)
        rightChild_index = self._rightChild(treeIndex)

        if quaryL > mid:
            return self._query(rightChild_index, mid+1, right, quaryL, quaryR)
        elif quaryR <= mid:
            return self._query(leftChild_index, left, mid, quaryL, quaryR)

        leftRes = self._query(leftChild_index, left, mid, quaryL, mid)
        rightRes = self._query(rightChild_index, mid+1, right, mid+1, quaryR)
        return self._merger(leftRes, rightRes)

    def _set(self, treeIndex, left, right, index, e):
        if left == right:
            self._tree[treeIndex] = e
            return

        mid = left + (right - left) // 2
        leftChild_index = self._leftChild(treeIndex)
        rightChild_index = self._rightChild(treeIndex)

        if index <= mid:
            self._set(leftChild_index, left, mid, index, e)
        else:
            self._set(rightChild_index, mid+1, right, index, e)

        self._tree[treeIndex] = self._merger(self._tree[leftChild_index], self._tree[rightChild_index])


def MoreOfficeHours(n, d, candidates):
    candidates.sort(key=lambda x: (x[1], x[2]))
    alist = list([float('inf') for _ in range(d+1)])
    segment_tree = SegmentTree(alist, merger_=lambda x, y: min(x, y))
    # segment_tree.printSegmentTree()

    for price, start, end in candidates:
        end = min(end, d)
        if start == 1:
            segment_tree.set(end, min(segment_tree.data[end], price))
        else:
            segment_tree.set(end, min(segment_tree.data[end], segment_tree.query(start-1, end) + price))

    if segment_tree.data[-1] == float('inf'):
        print(-1)
    else:
        print(segment_tree.data[-1])


if __name__ == '__main__':
    n, d = inlt()
    candidates = []
    for i in range(n):
        candidates.append(inlt())

    MoreOfficeHours(n, d, candidates)