from dataclasses import dataclass


# structure of Tree node
@dataclass
class Tree[node]:
    value: int
    left: node | None = None
    right: node | None = None


#main bst class
class BST:
    """
    # Binary Search Tree
    This is my implementation of Binary Search Tree with various functionalities.

    ## Attributes: 
    - `root` (Tree or None): Represents the root value of the tree, default None.
    
    ## Functions: 
    All private functions represent the actual implementation, while the public functions serve as a layer of abstraction to them.
    Without these functions, users would be required to create a global root variable and pass it to each and every function.
    Subsequently, when a function returns the root, the user would need to store that value in the global root variable.
    However, with my approach, there is no need to create a global root variable or pass it every time to a function.
    This results in a much cleaner code for the user.

    ### Private Functions: 
    - `__insert()`: Inserts the provided value to its appropriate location in BST.
    - `__inorder()`: Prints the inorder traversal of BST.
    - `__preorder()`: Prints the preorder traversal of BST.
    - `__postorder()`: Prints the postorder traversal of BST.
    - `__height()`: Returns the height\depth of the BST.
    - `__size()`: Returns size or number of elements in BST.
    - `__max()`: Returns the largest element of BST.
    - `__min()`: Returns the smallest element of BST.
    - `__remove()`: Removes an existing element from BST.
    - `__min_node()`: Returns the minimum node.

    ### Public Functions: 
    - `insert`, `inorder`, `preorder`, `postorder`, `height`, `size`, `max`, `min`, `remove`.
    These functions act as a layer of abstration for the private functions.

    ##### For more info about these functions look over the respective docstrings.

    ## Usage: 
    ```
    tree = BST()
    ```

    ## Example: 
    ```
    tree = BST()
    tree.insert(50)
    tree.inorder()
    # You can simply call other functions in a similar fashion. 
    ```

    ## Note:
    - I haven't added search function yet, so the program might show an unexpected behaviour if an element is already present while inserting, no elements present while traversing, etc.
    """
    def __init__(self) -> None:
        self.root: Tree | None = None

    def insert(self, val: int) -> None:
        """
        This function passes self.root to self.__insert() and while returning root it sets the value back to self.root.

        ## Parameters: 
        - val (int): The value to insert.

        ## Returns: 
        - None
        """
        self.root = self.__insert(self.root, val)

    def __insert(self, root: Tree | None, val: int) -> Tree:
        """
        This method inserts the given value to its respective location in BST. This is a recursive function.

        ## Parameters: 
        - `root` (Tree or None): self.root
        - val (int): Value to insert.

        ## Returns: 
        - Tree: A Tree object.
        """
        if not root:
            return Tree(val)

        elif root.value < val:
            root.right = self.__insert(root.right, val)

        else:
            root.left = self.__insert(root.left, val)

        return root
    
    def inorder(self) -> None:
        """
        This function passes self.root to self.__inorder().
        """
        self.__inorder(self.root)

    def __inorder(self, root: Tree | None) -> None:
        """
        Prints the inorder traversal of BST.
        """
        if root:
            self.__inorder(root.left)
            print(root.value, end='\t')
            self.__inorder(root.right)

    def preorder(self) -> None:
        """
        This function passes self.root to self.__preorder().
        """
        self.__preorder(self.root)

    def __preorder(self, root: Tree | None) -> None:
        """
        Prints the preorder traversal of BST.
        """
        if root:
            print(root.value, end='\t')
            self.__preorder(root.left)
            self.__preorder(root.right)

    def postorder(self) -> None:
        """
        This function passes self.root to self.__postorder().
        """
        self.__postorder(self.root)

    def __postorder(self, root: Tree | None) -> None:
        """
        Prints the postorder traversal of BST.
        """
        if root:
            self.__postorder(root.left)
            self.__postorder(root.right)
            print(root.value, end='\t')

    def height(self) -> int:
        """
        This function passes self.root to self.__height().
        """
        return self.__height(self.root)

    def __height(self, root: Tree | None) -> int:
        """
        Returns the height of BST.
        """
        if not root:
            return 0

        return 1 + max(self.__height(root.left), self.__height(root.right))

    def size(self) -> int:
        """
        This function passes self.root to self.__size().
        """
        return self.__size(self.root)

    def __size(self, root: Tree | None) -> int:
        """
        Returns the size of BST.
        """
        if not root:
            return 0

        return 1 + self.__size(root.left) + self.__size(root.right)
    
    def max(self) -> int:
        """
        This function passes self.root to self.__max().
        """
        return self.__max(self.root)

    def __max(self, root: Tree | None) -> int:
        """
        Returns the largest element of BST.
        """
        while root.right:
            root = root.right

        return root.value
    
    def min(self) -> int:
        """
        This function passes self.root to self.__min().
        """
        return self.__min(self.root)

    def __min(self, root: Tree | None) -> int:
        """
        Returns the smallest element of BST.
        """
        while root.left:
            root = root.left

        return root.value

    def __min_node(self, root: Tree | None) -> Tree:
        """
        Returns the node with minimum value.

        ## Parameters:
        - root (Tree or None): root node.

        ## Returns:
        - Tree: node with minimum value.
        """
        while root.left:
            root = root.left

        return root
    
    def remove(self, delete_value: int) -> None:
        """
        This method passes self.root and delete_value to self.__remove() and while returning root it sets the value back to self.root.
        """
        self.root = self.__remove(self.root, delete_value)

    def __remove(self, root: Tree | None, delete_value: int) -> Tree:
        """
        This recursive function removes the delete_value from the BST.
        """
        if not root:
            return root

        elif delete_value < root.value:
            root.left = self.__remove(root.left, delete_value)

        elif delete_value > root.value:
            root.right = self.__remove(root.right, delete_value)

        else:
            if not root.left:
                temp: Tree | None = root
                root = root.right
                del temp
                return root

            elif not root.right:
                temp: Tree | None = root
                root = root.left
                del temp
                return root

            else:
                temp: Tree | None = self.__min_node(root.right)
                root.value = temp.value
                root.right = self.__remove(root.right, temp.value)
                return root

        return root


if __name__ == '__main__':
    tree = BST()

    tree.insert(50)
    tree.insert(60)
    tree.insert(10)
    tree.insert(40)
    tree.insert(90)
    tree.insert(20)
    tree.insert(30)
    tree.insert(80)
    tree.insert(100)
    tree.insert(5)
    tree.insert(15)
    tree.insert(55)

    print("Inorder")
    tree.inorder()
    print("\nPreorder")
    tree.preorder()
    print("\npostorder")
    tree.postorder()

    print()
    print("height = ", tree.height())
    print(tree.size())
    print(tree.max(), tree.min())

    tree.remove(15)
    tree.remove(40)
    tree.remove(50)
    tree.inorder()
