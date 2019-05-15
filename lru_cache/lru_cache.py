from doubly_linked_list import DoublyLinkedList

class LRUCache:
  def __init__(self, limit=10):
    self.limit = limit
    self.length = 0
    self.doubly_linked_list = DoublyLinkedList()

  """
  Retrieves the value associated with the given key. Also
  needs to move the key-value pair to the top of the order
  such that the pair is considered most-recently used.
  Returns the value associated with the key or None if the
  key-value pair doesn't exist in the cache. 
  """
  def get(self, key):
    exists = self.doubly_linked_list.get_item(key)
    if exists:
      self.doubly_linked_list.move_to_front(exists)
      return exists.value[key]

  """
  Adds the given key-value pair to the cache. The newly-
  added pair should be considered the most-recently used
  entry in the cache. If the cache is already at max capacity
  before this entry is added, then the oldest entry in the
  cache needs to be removed to make room. Additionally, in the
  case that the key already exists in the cache, we simply 
  want to overwrite the old value associated with the key with
  the newly-specified value. 
  """
  def set(self, key, value):
    exists = self.doubly_linked_list.get_item(key)
    if exists:
      exists.value[key] = value
      self.doubly_linked_list.move_to_front(exists)
    else:
      self.doubly_linked_list.add_to_head({key: value})
      self.length += 1
      if self.length > self.limit:
        self.doubly_linked_list.remove_from_tail()
        
