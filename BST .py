class Node:
    """Represents a single node in the Binary Search Tree."""
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:
    """Implements a Binary Search Tree with its standard operations."""
    def __init__(self):
        self.root = None

    # --- INSERTION ---
    def insert(self, key):
        """Public method to insert a key into the BST."""
        self.root = self._insert_recursive(self.root, key)

    def _insert_recursive(self, root, key):
        # Base case: If the tree/subtree is empty, return a new node
        if root is None:
            return Node(key)

        # Recur down the tree
        if key < root.key:
            root.left = self._insert_recursive(root.left, key)
        elif key > root.key:
            root.right = self._insert_recursive(root.right, key)
        
        # Return the unchanged node pointer
        return root

    # --- SEARCH ---
    def search(self, key):
        """Public method to search for a key. Returns True if found, False otherwise."""
        return self._search_recursive(self.root, key) is not None

    def _search_recursive(self, root, key):
        # Base Cases: root is null or key is present at root
        if root is None or root.key == key:
            return root

        # Key is smaller than root's key
        if key < root.key:
            return self._search_recursive(root.left, key)

        # Key is greater than root's key
        return self._search_recursive(root.right, key)

    # --- DELETION ---
    def delete(self, key):
        """Public method to delete a key from the BST."""
        self.root = self._delete_recursive(self.root, key)

    def _delete_recursive(self, root, key):
        # Base Case
        if root is None:
            return root

        # Recur down the tree to locate the node
        if key < root.key:
            root.left = self._delete_recursive(root.left, key)
        elif key > root.key:
            root.right = self._delete_recursive(root.right, key)
        else:
            # Node to be deleted found!

            # Case 1 & 2: Node with only one child or no child (leaf)
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # Case 3: Node with two children.
            # Get the inorder successor (smallest in the right subtree)
            root.key = self._min_value_node(root.right).key

            # Delete the inorder successor
            root.right = self._delete_recursive(root.right, root.key)

        return root

    def _min_value_node(self, node):
        """Helper to find the node with the minimum value in a subtree."""
        current = node
        while current.left is not None:
            current = current.left
        return current

    # --- TRAVERSALS ---
    def inorder(self):
        """Left -> Root -> Right (Produces sorted order for BST)"""
        res = []
        self._inorder_recursive(self.root, res)
        return res

    def _inorder_recursive(self, root, res):
        if root:
            self._inorder_recursive(root.left, res)
            res.append(root.key)
            self._inorder_recursive(root.right, res)

    def preorder(self):
        """Root -> Left -> Right"""
        res = []
        self._preorder_recursive(self.root, res)
        return res

    def _preorder_recursive(self, root, res):
        if root:
            res.append(root.key)
            self._preorder_recursive(root.left, res)
            self._preorder_recursive(root.right, res)

    def postorder(self):
        """Left -> Right -> Root"""
        res = []
        self._postorder_recursive(self.root, res)
        return res

    def _postorder_recursive(self, root, res):
        if root:
            self._postorder_recursive(root.left, res)
            self._postorder_recursive(root.right, res)
            res.append(root.key)


# --- EXECUTABLE DEMONSTRATION ---
if __name__ == "__main__":
    bst = BinarySearchTree()

    # 1. Elements insertion
    elements = [50, 30, 20, 40, 70, 60, 80]
    print(f"Inserting elements: {elements}")
    for el in elements:
        bst.insert(el)

    # 2. Display Traversals
    print("\n--- Tree Traversals ---")
    print(f"In-order Traversal   (Sorted) : {bst.inorder()}")
    print(f"Pre-order Traversal           : {bst.preorder()}")
    print(f"Post-order Traversal          : {bst.postorder()}")

    # 3. Search Operations
    print("\n--- Search Operations ---")
    for target in [40, 90]:
        print(f"Searching for {target}: {'Found' if bst.search(target) else 'Not Found'}")

    # 4. Deletion Operations
    print("\n--- Deletion Operations ---")
    print("Deleting 20 (Leaf node)...")
    bst.delete(20)
    print(f"In-order after deleting 20: {bst.inorder()}")

    print("\nDeleting 30 (Node with single child)...")
    bst.delete(30)
    print(f"In-order after deleting 30: {bst.inorder()}")

    print("\nDeleting 50 (Root node with two children)...")
    bst.delete(50)
    print(f"In-order after deleting 50: {bst.inorder()}")
