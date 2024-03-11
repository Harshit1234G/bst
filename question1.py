"""
QUESTION 1: As a senior backend engineer at Jovian, you are tasked with developing a fast in-memory data structure to manage profile information (username, name and email) for 100 million users. It should allow the following operations to be performed efficiently:

1. Insert the profile information for a new user.
2. Find the profile information of a user, given their username
3. Update the profile information of a user, given their usrname
4. List all the users of the platform, sorted by username
You can assume that usernames are unique.
"""

#link: https://jovian.com/aakashns/python-binary-search-trees

# we have to create a data structure which can store 100 million datas and perform insert, find, update, list functions.

from dataclasses import dataclass


@dataclass
class User:
    username: str
    name: str
    email: str


# Brute force
# time complexity: O(n) for all funcs
class UserDatabase:
    def __init__(self) -> None:
        self.users: list[User] = []

    def insert(self, user: User) -> None:
        if self.find(user.username):
            print(f"'{user.username}' username already exists.")
            return 
        
        for index, u in enumerate(self.users):
            if u.username > user.username:
                self.users.insert(index, user)
                break

        else:
            self.users.append(user)

    def find(self, username: str) -> User | None:
        for user in self.users:
            if user.username == username:
                return user
            
        return None

    def update(self, user: User) -> None:
        target = self.find(user.username)
        if target:
            target.name = user.name
            target.email = user.email

        else:
            print(f"'{user.username}' username doesn't exists.")

    def list_all(self) -> None:
        if not len(self.users):
            print('Database empty.')
            return 
        
        for index, user in enumerate(self.users):
            print(f'{index + 1}. {user}')


if __name__ == '__main__':
    aakash = User('aakash', 'Aakash Rai', 'aakash@example.com')
    biraj = User('biraj', 'Biraj Das', 'biraj@example.com')
    hemanth = User('hemanth', 'Hemanth Jain', 'hemanth@example.com')
    jadhesh = User('jadhesh', 'Jadhesh Verma', 'jadhesh@example.com')
    siddhant = User('siddhant', 'Siddhant Sinha', 'siddhant@example.com')
    sonaksh = User('sonaksh', 'Sonaksh Kumar', 'sonaksh@example.com')
    vishal = User('vishal', 'Vishal Goel', 'vishal@example.com')

    udb = UserDatabase()
    udb.insert(aakash)
    udb.insert(vishal)
    udb.insert(biraj)
    udb.insert(jadhesh)
    udb.insert(sonaksh)
    udb.insert(siddhant)
    udb.insert(hemanth)
    udb.insert(hemanth)
    udb.list_all()
    print(udb.find('aakash'))
    print(udb.find('123'))
    udb.update(User('aakash', 'Aakash Gupta', 'aakash@gmail.com'))
    udb.update(User('124', 'Aakash Gupta', 'aakash@gmail.com'))
    udb.list_all()