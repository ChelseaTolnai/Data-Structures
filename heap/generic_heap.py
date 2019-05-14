import math


def max_heap(x, y):
  return True if x > y else False


class Heap:
  def __init__(self, comparator=max_heap):
    self.storage = []
    self.comparator = comparator

  def insert(self, value):
    self.storage += [value]
    self._bubble_up(len(self.storage)-1)

  def delete(self):
    priority_value = self.get_priority()
    if priority_value is None:
      return
    self.storage[0], self.storage[-1] = self.storage[-1], self.storage[0]
    self.storage.pop()
    self._sift_down(0)
    return priority_value

  def get_priority(self):
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
    x = self.storage[index]
    y = self.storage[parent_index]
    if self.comparator(x, y):
      self.storage[parent_index], self.storage[index] = self.storage[index], self.storage[parent_index]
      return self._bubble_up(parent_index)

  def _sift_down(self, index):
    left_index = 2*index + 1
    right_index = 2*index + 2

    if left_index >= len(self.storage):
      return

    priority_index = left_index \
                if right_index >= len(self.storage) \
                  or self.comparator(self.storage[left_index], self.storage[right_index]) \
                else right_index

    x = self.storage[priority_index]
    y = self.storage[index]

    if self.comparator(x, y):
      self.storage[index], self.storage[priority_index] = self.storage[priority_index], self.storage[index]
      return self._sift_down(priority_index)

