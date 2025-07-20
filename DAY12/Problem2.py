def requireAdmin(func):
    """
    A decorator that only allows a function to execute if a _user dictionary
    has the role 'admin'. If the user is not an admin, prints 'Access Denied'.
    """
    def wrapper(userId):
        global user 

        if 'role' in user and user['role'] == 'admin':
            return func(userId)
        else:
            print("Access Denied")
    return wrapper
@requireAdmin
def deleteUser(userId):
    print(f"User {userId} deleted")
user = {'username': 'Ramlinga Raju', 'role': 'admin'}
print(f"Current user: {user['username']} ({user['role']})")
deleteUser(100)
print("-" * 20)
user = {'username': 'Bantu Reddy', 'role': 'user'}
print(f"Current user: {user['username']} ({user['role']})")
deleteUser(200)
print("-" * 20)
user = {'username': 'Guest'}
print(f"Current user: {user['username']} (no role specified)")
deleteUser(300)
print("-" * 20)
user = {'username': 'Moderator', 'role': 'moderator'}
print(f"Current user: {user['username']} ({user['role']})")
deleteUser(400)
print("-" * 20)