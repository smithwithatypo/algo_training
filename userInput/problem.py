# Rep 1/4 - Tree DFS


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder_traversal(root):
    """
    Return inorder traversal (left, root, right).
    Tree:    2
           /   \
          1     3
    Result: [1, 2, 3]
    """
    # your code here
    pass

def test_inorder_traversal():
    root = TreeNode(2, TreeNode(1), TreeNode(3))
    assert inorder_traversal(root) == [1, 2, 3]
    
    root = TreeNode(1)
    assert inorder_traversal(root) == [1]
    
    assert inorder_traversal(None) == []
