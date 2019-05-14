import math


class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    self.storage += [value]
    self._bubble_up(len(self.storage)-1)

  def delete(self):
    max_value = self.get_max()
    self.storage[0], self.storage[-1] = self.storage[-1], self.storage[0]
    self.storage.pop()
    self._sift_down(0)
    return max_value

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    if index == 0:
      return

    parent_index = math.floor((index-1) / 2)
    if self.storage[index] > self.storage[parent_index]:
      self.storage[parent_index], self.storage[index] = self.storage[index], self.storage[parent_index]
      return self._bubble_up(parent_index)

  def _sift_down(self, index):
    left_index = 2*index + 1    # (0) => 1
    right_index = 2*index + 2   # (0) => 2
    pass


heap = Heap()

heap.insert(6)
print(heap.storage == [6])
heap.insert(8)
print(heap.storage == [8, 6])
heap.insert(10)
print(heap.storage == [10, 6, 8])
heap.insert(9)
print(heap.storage == [10, 9, 8, 6])
heap.insert(1)
print(heap.storage == [10, 9, 8, 6, 1])
heap.insert(9)
print(heap.storage == [10, 9, 9, 6, 1, 8])
heap.insert(9)
print(heap.storage == [10, 9, 9, 6, 1, 8, 9])
heap.insert(5) 
print(heap.storage == [10, 9, 9, 6, 1, 8, 9, 5])

"""
10
|  \
9   9
|\  |\
6 1 8 9
|
5

l = 2i + 1
r = 2i + 2
p = floor( (i-1) / 2 )
"""