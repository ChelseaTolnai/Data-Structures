"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next

  """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""
  def insert_after(self, value):
    current_next = self.next
    self.next = ListNode(value, self, current_next)
    if current_next:
      current_next.prev = self.next

  """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""
  def insert_before(self, value):
    current_prev = self.prev
    self.prev = ListNode(value, current_prev, self)
    if current_prev:
      current_prev.next = self.prev

  """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""
  def delete(self):
    if self.prev:
      self.prev.next = self.next
    if self.next:
      self.next.prev = self.prev

"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node
    self.length = 1 if node is not None else 0

  def __len__(self):
    return self.length

  def add_to_head(self, value):
    if self.length == 0:
      node = ListNode(value)
      self.head = node
      self.tail = node
    else:
      self.head.insert_before(value)
      self.head = self.head.prev
    self.length += 1

  def remove_from_head(self):
    prev_head = self.head
    if self.length == 0:
      return 
    else:
      new_head = self.head.next
      self.head.delete()
      self.head = new_head
      self.tail = self.tail if self.head is not None else None
      self.length -= 1

    return prev_head.value if prev_head is not None else prev_head

  def add_to_tail(self, value):
    if self.length == 0:
      node = ListNode(value)
      self.head = node
      self.tail = node
    else:
      self.tail.insert_after(value)
      self.tail = self.tail.next
    self.length += 1

  def remove_from_tail(self):
    prev_tail = self.tail
    if self.length == 0:
      return 
    else:
      new_tail = self.tail.prev
      self.tail.delete()
      self.tail = new_tail
      self.head = self.head if self.tail is not None else None
      self.length -= 1

    return prev_tail.value if prev_tail is not None else prev_tail

  def move_to_front(self, node):
    if self.length > 1 and node != self.head:
      current_node = node
      node.delete()
      self.head.insert_before(current_node.value)
      self.head = self.head.prev
      self.tail = self.tail if node != self.tail else current_node.prev

  def move_to_end(self, node):
    if self.length > 1 and node != self.tail:
      current_node = node
      node.delete()
      self.tail.insert_after(current_node.value)
      self.tail = self.tail.next
      self.head = self.head if node != self.head else current_node.next

  def delete(self, node):
    current_node = node
    node.delete()
    self.head = self.head if node != self.head else current_node.next
    self.tail = self.tail if node != self.tail else current_node.prev
    self.length -= 1

  def get_max(self):
    current_node = self.head
    max_node = self.head
    while current_node:
      if current_node.value > max_node.value:
        max_node = current_node
      current_node = current_node.next
    return max_node.value if self.head is not None else None

  def get_item(self, key):
    current_node = self.head
    while current_node:
      if current_node.value.get(key):
        return current_node
      current_node = current_node.next
    return None