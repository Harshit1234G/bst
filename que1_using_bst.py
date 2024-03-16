from dataclasses import dataclass


# structure of Tree node
@dataclass
class Tree[node]:
    username: str
    name: str
    email: str
    left: node | None = None
    right: node | None = None


class BST:
    def __init__(self) -> None:
        self.root: Tree | None = None

    def insert(self, username: str, name: str, email: str) -> None:
        self.root = self.__insert(self.root, username, name, email)

    def __insert(self, root: Tree | None, username: str, name: str, email: str) -> Tree:
        if not root:
            return Tree(username, name, email)

        elif root.username < username:
            root.right = self.__insert(root.right, username, name, email)

        else:
            root.left = self.__insert(root.left, username, name, email)

        return root
    
    def find(self, search_username: str) -> Tree | None:
        return self.__find(self.root, search_username)

    def __find(self, root: Tree | None, search_username: str) -> Tree | None:
        if not root:
            return None
        
        if search_username == root.username:
            return root
        
        elif search_username < root.username:
            root = self.__find(root.left, search_username)

        else:
            root = self.__find(root.right, search_username)

        return root
    
    def update(self, username: str, name: str, email: str) -> None:
        root = self.find(username)
        if root:
            root.name = name
            root.email = email

    def list_all(self) -> None:
        self.__list_all(self.root)

    def __list_all(self, root: Tree | None) -> None:
        if root:
            self.__list_all(root.left)
            print(f"Username: {root.username}\nName: {root.name}\nEmail: {root.email}\n")
            self.__list_all(root.right)


if __name__ == '__main__':
    tree = BST()
    tree.insert("harshit", 'Harshit Kumawat', 'harshit@gmail.com')
    tree.insert('biraj', 'Biraj Das', 'biraj@example.com')
    tree.insert('aakash', 'Aakash Rai', 'aakash@example.com')
    tree.insert('jadhesh', 'Jadhesh Verma', 'jadhesh@example.com')
    tree.insert('hemanth', 'Hemanth Jain', 'hemanth@example.com')
    tree.insert('siddhant', 'Siddhant Sinha', 'siddhant@example.com')
    tree.insert('vishal', 'Vishal Goel', 'vishal@example.com')
    tree.insert('sonaksh', 'Sonaksh Kumar', 'sonaksh@example.com')

    tree.list_all()

    print(tree.find('harshit').name, tree.find('asdfasdf'))

    tree.update('biraj', 'Biraj Kumar', 'biraj1234@gmail.com')

    biraj = tree.find('biraj')

    print(biraj.name, biraj.email)
