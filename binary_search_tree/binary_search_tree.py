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
      branch.insert(value)

  def contains(self, target):
    pass

  def get_max(self):
    pass

  def for_each(self, cb):
    pass


bst = BinarySearchTree(5)

bst.insert(2)
bst.insert(3)
bst.insert(7)
bst.insert(6)
print(bst.left.right.value == 3)
print(bst.right.left.value == 6)