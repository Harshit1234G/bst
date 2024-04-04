#Write a function to create a balanced BST from a sorted list/array of integers.

from dataclasses import dataclass


# structure of Tree node
@dataclass
class Tree[node]:
    value: int
    left: node | None = None
    right: node | None = None


def make_balanced_bst(data: list[int]) -> Tree:
    if not data:
        return None

    mid = len(data) // 2
    root = Tree(data[mid])
    root.left = make_balanced_bst(data[:mid])
    root.right = make_balanced_bst(data[mid+1:])
    return root

def display(
        root: Tree | None,
        space: str = '\t',
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
    display(root.right, space, level + 1)
    print(space * level, root.value, sep='')
    display(root.left, space, level + 1)

tree = make_balanced_bst(list(range(10)))
display(tree)