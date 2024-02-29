from dataclasses import dataclass


@dataclass
class Tree[node]:
    value: int
    left: node | None = None
    right: node | None = None


class BST:
    def __init__(self) -> None:
        self.root: Tree | None = None

    def insert(self, val: int) -> None:
        self.root = self.__insert(self.root, val)

    def __insert(self, root: Tree | None, val: int) -> Tree:
        if not root:
            return Tree(val)

        elif root.value < val:
            root.right = self.__insert(root.right, val)

        else:
            root.left = self.__insert(root.left, val)

        return root
    
    def inorder(self) -> None:
        self.__inorder(self.root)

    def __inorder(self, root: Tree | None) -> None:
        if root:
            self.__inorder(root.left)
            print(root.value, end='\t')
            self.__inorder(root.right)

    def preorder(self) -> None:
        self.__preorder(self.root)

    def __preorder(self, root: Tree | None) -> None:
        if root:
            print(root.value, end='\t')
            self.__preorder(root.left)
            self.__preorder(root.right)

    def postorder(self) -> None:
        self.__postorder(self.root)

    def __postorder(self, root: Tree | None) -> None:
        if root:
            self.__postorder(root.left)
            self.__postorder(root.right)
            print(root.value, end='\t')

    def height(self) -> int:
        return self.__height(self.root)

    def __height(self, root: Tree | None) -> int:
        if not root:
            return 0

        return 1 + max(self.__height(root.left), self.__height(root.right))

    def size(self) -> int:
        return self.__size(self.root)

    def __size(self, root: Tree | None) -> int:
        if not root:
            return 0

        return 1 + self.__size(root.left) + self.__size(root.right)
    
    def max(self) -> int:
        return self.__max(self.root)

    def __max(self, root: Tree | None) -> int:
        while root.right:
            root = root.right

        return root.value
    
    def min(self) -> int:
        return self.__min(self.root)

    def __min(self, root: Tree | None) -> int:
        while root.left:
            root = root.left

        return root.value

    def __min_node(self, root: Tree | None) -> Tree:
        while root.left:
            root = root.left

        return root
    
    def remove(self, delete_value: int) -> None:
        self.root = self.__remove(self.root, delete_value)

    def __remove(self, root: Tree | None, delete_value: int) -> Tree:
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
