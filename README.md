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
  - By default the self.insert() will take repeated values. If you don't want repeated values use self.search() before inserting. If node already present prompt user about it, else insert.
  - If no value present in BST then inorder, preorder, and postorder will print nothing without prompting anything.
  - If delete_value of self.remove() is not present in BST then the function will do nothing without prompting.
