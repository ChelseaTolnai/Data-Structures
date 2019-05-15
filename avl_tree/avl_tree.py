"""
Node class to keep track of
the data internal to individual nodes
"""
class Node:
  def __init__(self, key):
    self.key = key
    self.left = None
    self.right = None

"""
A tree class to keep track of things like the
balance factor and the rebalancing logic
"""
class AVLTree:
  def __init__(self, node=None):
    self.node = node
    # init height to -1 because of 0-indexing
    self.height = -1
    self.balance = 0

  """
  Display the whole tree. Uses recursive def.
  """
  def display(self, level=0, pref=''):
    self.update_height()  # Update height before balancing
    self.update_balance()
    
    if self.node != None: 
      print ('-' * level * 2, pref, self.node.key,
        f'[{self.height}:{self.balance}]',
        'L' if self.height == 0 else ' ')
      if self.node.left != None:
        self.node.left.display(level + 1, '<')
      if self.node.right != None:
        self.node.right.display(level + 1, '>')

  """
  Computes the maximum number of levels there are
  in the tree
  """
  def update_height(self):
    if self.node:
      self.height = max(self.node.left.update_height() if self.node.left else -1, \
                        self.node.right.update_height() if self.node.right else -1) \
                        + 1
    return self.height

  """
  Updates the balance factor on the AVLTree class
  """
  def update_balance(self):
    if self.node:
      self.balance = (self.node.left.update_balance() if self.node.left else 0) - \
                     (self.node.right.update_balance() if self.node.right else 0)
      return self.height
    else:
      return self.balance

  """
  Perform a left rotation, making the right child of this
  node the parent and making the old parent the left child
  of the new parent. 
  """
  def left_rotate(self):
    old_parent = self.node
    new_parent = old_parent.right
    new_parent_left_child = new_parent.node.left
    self.node = new_parent.node
    new_parent.node = new_parent_left_child.node
    new_parent_left_child.node = old_parent

    self.update_height()
    self.update_balance()

  """
  Perform a right rotation, making the left child of this
  node the parent and making the old parent the right child
  of the new parent. 
  """
  def right_rotate(self):
    old_parent = self.node
    new_parent = old_parent.left
    new_parent_right_child = new_parent.node.right
    self.node = new_parent.node
    new_parent.node = new_parent_right_child.node
    new_parent_right_child.node = old_parent

    self.update_height()
    self.update_balance()

  """
  Sets in motion the rebalancing logic to ensure the
  tree is balanced such that the balance factor is
  1 or -1
  """
  def rebalance(self):
    self.update_height()
    self.update_balance()

    while self.balance < -1 or self.balance > 1:  # while parent unbalanced
      if self.balance > 1:  # if parent left heavy
        if self.node.left.balance < 0:  # if parent left heavy and left_child right heavy
          self.node.left.left_rotate()  # then left rotate left_child
        self.right_rotate()  # else right rotate parent
      if self.balance < -1: # if parent right heavy
        if self.node.right.balance > 0:  # if parent right heavy and right_child left heavy
          self.node.right.right_rotate() # then right rotate right_child
        self.left_rotate()  # else left rotate parent
    
  """
  Uses the same insertion logic as a binary search tree
  after the value is inserted, we need to check to see
  if we need to rebalance
  """
  def insert(self, key):
    pass


"""
balanceFactor = height(left subtree) - height(right subtree)
"""

tree = AVLTree()

tree.node = Node(5)
tree.node.right = AVLTree(Node('x'))
tree.node.left = AVLTree(Node(3))
tree.node.left.node.right = AVLTree(Node(4))
tree.node.left.node.left = AVLTree(Node('c'))
tree.node.left.node.right.node.left = AVLTree(Node('y'))
tree.node.left.node.right.node.right = AVLTree(Node('z'))

tree.display()
print("***")
tree.rebalance()
tree.display()


# assertEqual(tree.node.key, 4)
# assertEqual(tree.node.left.node.key, 3)
# assertEqual(tree.node.right.node.key, 5)
# assertEqual(tree.node.left.node.left.node.key, 'c')
# assertEqual(tree.node.left.node.right.node.key, 'y') 
# assertEqual(tree.node.right.node.left.node.key, 'z')
# assertEqual(tree.node.right.node.right.node.key, 'x') 


# tree.display()