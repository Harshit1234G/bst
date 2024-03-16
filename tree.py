from dataclasses import dataclass

type NodeOrNone = TreeNode | None


@dataclass
class TreeNode:
    value: int
    left: NodeOrNone = None
    right: NodeOrNone = None


class BinaryTree:
    """
    It is a basic implementation of Binary Tree.
    """
    root: NodeOrNone = None

    def __init__(self, data: tuple) -> None:
        self.root = self.__parse_tuple(data)

    def __parse_tuple(self, data: tuple | int | None) -> NodeOrNone:
        if isinstance(data, tuple) and len(data) == 3:
            node = TreeNode(data[1])
            node.left = self.__parse_tuple(data[0])
            node.right = self.__parse_tuple(data[2])

        elif not data:
            node = None

        else:
            node = TreeNode(data)

        return node

    def display(self, space: str = '\t') -> None:
        self.__display(self.root, space)

    def __display(
        self,
        root: NodeOrNone,
        space: str,
        level: int = 0
    ) -> None:
        # if root is empty
        if not root:
            print(space * level, None, sep='')
            return None

        # if root is a leaf node
        if not root.right and not root.left:
            print(space * level, root.value, sep='')
            return None

        # if root has child
        self.__display(root.right, space, level + 1)
        print(space * level, root.value, sep='')
        self.__display(root.left, space, level + 1)

    def to_pytuple(self) -> tuple:
        return self.__to_pytuple(self.root)

    def __to_pytuple(self, root: NodeOrNone) -> tuple:
        if not root:
            return None
        
        if not root.left and not root.right:
            return root.value
        
        return self.__to_pytuple(root.left), root.value, self.__to_pytuple(root.right)
    
    def inorder(self) -> list[int]:
        return self.__inorder(self.root)

    def __inorder(self, root: NodeOrNone) -> list[int]:
        if not root:
            return []
        
        return self.__inorder(root.left) + [root.value] + self.__inorder(root.right)

    def is_bst(self) -> bool:
        tree_list = self.inorder()

        for i in range(len(tree_list) - 1):
            if tree_list[i] > tree_list[i + 1]:
                return False
            
        return True
    
    def is_balanced(self) -> tuple[bool, int]:
        return self.__is_balanced(self.root)
    
    def __is_balanced(self, root: NodeOrNone) -> tuple[bool, int]:
        if not root:
            return True, 0
        
        balanced_l, height_l = self.__is_balanced(root.left)
        balanced_r, height_r = self.__is_balanced(root.right)

        balanced = balanced_l and balanced_r and abs(height_l - height_r) <= 1
        height = 1 + max(height_r, height_l)

        return balanced, height

    def __str__(self) -> str:
        return str(self.root)


if __name__ == '__main__':
    tree = BinaryTree(((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8))))
    print(tree)
    tree.display()
    print(tree.to_pytuple())
    print(tree.inorder())
    print(tree.is_bst())
    
    tree2 = BinaryTree(((5, 10, 40), 50, (55, 60, 90)))
    print(tree2.inorder())
    print(tree2.is_bst())

    # it also works for strings
    tree3 = BinaryTree((('aakash', 'biraj', 'hemanth')  , 'jadhesh', ('siddhant', 'sonaksh', 'vishal')))
    tree3.display()
    print(tree3.is_bst())

    tree4 = BinaryTree((None, 2, (None, 3, (None, 4, (None, 5, None)))))
    tree4.display()
    
    print(tree.is_balanced())
    print(tree2.is_balanced())
    print(tree3.is_balanced())
    print(tree4.is_balanced())