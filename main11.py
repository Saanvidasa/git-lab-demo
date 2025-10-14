# greeting.py
def greet_user(name):
    """
    Function to greet the user with their name.
    """
    return f"Hello, {name}! Welcome to Git + Python demo."

if __name__ == "__main__":
    user_name = input("Enter your name: ")
    print(greet_user(user_name))
