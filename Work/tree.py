class Node:
    def __init__(self, data):
        """
        The constructor for the Node class.
        This function creates a new Node object and sets its data value to the input data.
        It also sets the left and right pointers to None.
        :param data: The value to store in the node.
        """
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        """
        The constructor for the BinaryTree class.
        This function creates a new BinaryTree object and sets its root to None.
        """
        self.root = None

    def insert(self, data):
        """
        Inserts a new node with the input data into the binary tree.
        :param data: The value to insert into the tree.
        """
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
            return
        current = self.root
        while True:
            if data <= current.data:
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right


if __name__ == '__main__':
    """
    5
    ├── 3
    └── 7
        ├── 1
        └── 9
    """
    # Create a new binary tree object
    bt = BinaryTree()
    # Insert some data into the tree
    bt.insert(5)
    bt.insert(3)
    bt.insert(7)
    bt.insert(1)
    bt.insert(9)
    
    # Print the data of the root node
    print(bt.root.data)  # Output: 5
    
    # Print the data of the left child of the root node
    print(bt.root.left.data)  # Output: 3
    
    # Print the data of the right child of the root node
    print(bt.root.right.data)  # Output: 7