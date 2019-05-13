class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if value < self.value and self.left is None:
      self.left = BinarySearchTree(value)
    elif value >= self.value and self.right is None:
      self.right = BinarySearchTree(value)
    else:
      branch = self.left if value < self.value else self.right
      return branch.insert(value)

  def contains(self, target):
    branch = self.left if target < self.value else self.right
    if self.value == target:
      return True
    elif branch is None:
      return False
    else:
      return branch.contains(target)

  def get_max(self):
    max_value = self.value
    while self.right:
      return self.right.get_max()
    return max_value

  def for_each(self, cb):
    cb(self.value)
    while self.left:
      return self.left.for_each(cb)
    while self.right:
      return self.right.for_each(cb)


bst = BinarySearchTree(5)

bst.insert(2)
bst.insert(3)
bst.insert(7)
bst.insert(6)
print(bst.left.right.value == 3)  # True
print(bst.right.left.value == 6)  # True

print(bst.contains(5))  # True
print(bst.contains(6))  # True
print(bst.contains(8))  # False

print(bst.get_max() == 7)   # True
bst.insert(10)
print(bst.get_max() == 7)   # False
print(bst.get_max() == 10)   # True
