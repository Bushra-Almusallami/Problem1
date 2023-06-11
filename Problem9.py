# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Function to check if two trees are identical
def is_identical(root1, root2):
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None:
        return False
    return (root1.val == root2.val and
            is_identical(root1.left, root2.left) and
            is_identical(root1.right, root2.right))

# Function to check if tree1 is a subtree of tree2
def is_subtree(tree1, tree2):
    if tree1 is None:
        return True
    if tree2 is None:
        return False
    if is_identical(tree1, tree2):
        return True
    return is_subtree(tree1, tree2.left) or is_subtree(tree1, tree2.right)

# Function to display the tree diagram
def display_tree(root, indent=''):
    if root is None:
        return
    print(indent + str(root.val))
    display_tree(root.left, indent + '  |')
    display_tree(root.right, indent + '  |')

# Example usage
# Tree 1
t1 = TreeNode(10)
t1.left = TreeNode(4)
t1.right = TreeNode(6)
t1.left.right = TreeNode(30)

# Tree 2
t2 = TreeNode(26)
t2.left = TreeNode(10)
t2.right = TreeNode(3)
t2.left.left = TreeNode(4)
t2.left.right = TreeNode(6)
t2.right.right = TreeNode(3)
t2.left.left.right = TreeNode(30)

print("Tree 1:")
display_tree(t1)
print("\nTree 2:")
display_tree(t2)

if is_subtree(t1, t2):
    print("\nTree one is a subtree of tree two.")
else:
    print("\nTree one is not a subtree of tree two")
