
class Node:
   def __init__(self, val, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

def serialize(root):
    if (root != None):
        result = root.val, serialize(root.left), serialize(root.right)
        return list(result)
    return None

def deserialize(s):
    if s:
        val = s.pop(0)
        if (val != None):
            root = Node(val)
            root.left = deserialize(s)
            root.right = deserialize(s)
            return root
        else:
            return None
    return None

node = Node('root', Node('left', Node('left.left')), Node('right'))


print(deserialize(serialize(node)).left.val)

