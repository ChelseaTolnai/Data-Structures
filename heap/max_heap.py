import math


class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    self.storage += [value]
    self._bubble_up(len(self.storage)-1)

  def delete(self):
    max_value = self.get_max()
    if max_value is None:
      return
    self.storage[0], self.storage[-1] = self.storage[-1], self.storage[0]
    self.storage.pop()
    self._sift_down(0)
    return max_value

  def get_max(self):
    if len(self.storage) > 0:
      return self.storage[0]
    else:
      return None

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
    left_index = 2*index + 1
    right_index = 2*index + 2

    if left_index >= len(self.storage):
      return

    max_index = left_index \
                if right_index >= len(self.storage) \
                   or self.storage[left_index] > self.storage[right_index] \
                else right_index
    if self.storage[index] < self.storage[max_index]:
      self.storage[max_index], self.storage[index] = self.storage[index], self.storage[max_index]
      return self._sift_down(max_index)

"""
heap = Heap()

heap.insert(6)
print(heap.storage == [6])
print(heap.get_max() == 6)
print(heap.get_size() == 1)
heap.insert(8)
print(heap.storage == [8, 6])
print(heap.get_max() == 8)
print(heap.get_size() == 2)
heap.insert(10)
print(heap.storage == [10, 6, 8])
print(heap.get_max() == 10)
print(heap.get_size() == 3)
heap.insert(9)
print(heap.storage == [10, 9, 8, 6])
print(heap.get_max() == 10)
print(heap.get_size() == 4)
heap.insert(1)
print(heap.storage == [10, 9, 8, 6, 1])
print(heap.get_max() == 10)
print(heap.get_size() == 5)
heap.insert(9)
print(heap.storage == [10, 9, 9, 6, 1, 8])
print(heap.get_max() == 10)
print(heap.get_size() == 6)
heap.insert(9)
print(heap.storage == [10, 9, 9, 6, 1, 8, 9])
print(heap.get_max() == 10)
print(heap.get_size() == 7)
heap.insert(5) 
print(heap.storage == [10, 9, 9, 6, 1, 8, 9, 5])
print(heap.get_max() == 10)
print(heap.get_size() == 8)
"""

"""
heap = Heap()

heap.insert(6)
heap.insert(7)
heap.insert(5)
heap.insert(8)
heap.insert(10)
heap.insert(1)
heap.insert(2)
heap.insert(5)
print(heap.storage == [10, 8, 5, 6, 7, 1, 2, 5])
print(heap.get_max() == 10)
print(heap.get_size() == 8)

print(heap.delete() == 10)
print(heap.storage == [8, 7, 5, 6, 5, 1, 2])
print(heap.get_max() == 8)
print(heap.get_size() == 7)

print(heap.delete() == 8)
print(heap.storage == [7, 6, 5, 2, 5, 1])
print(heap.get_max() == 7)
print(heap.get_size() == 6)

print(heap.delete() == 7)
print(heap.storage == [6, 5, 5, 2, 1])
print(heap.get_max() == 6)
print(heap.get_size() == 5)

print(heap.delete() == 6)
print(heap.storage == [5, 5, 1, 2])
print(heap.get_max() == 5)
print(heap.get_size() == 4)

print(heap.delete() == 5)
print(heap.storage == [5, 2, 1])
print(heap.get_max() == 5)
print(heap.get_size() == 3)

print(heap.delete() == 5)
print(heap.storage == [2, 1])
print(heap.get_max() == 2)
print(heap.get_size() == 2)

print(heap.delete() == 2)
print(heap.storage == [1])
print(heap.get_max() == 1)
print(heap.get_size() == 1)

print(heap.delete() == 1)
print(heap.storage == [])
print(heap.get_max() is None)
print(heap.get_size() == 0)

print(heap.delete() is None)
print(heap.storage == [])
print(heap.get_max() is None)
print(heap.get_size() == 0)
"""