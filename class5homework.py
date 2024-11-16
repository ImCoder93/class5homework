usernames = ["Alice", "Bob", "Charlie", "David"]

input_username = input("Enter your username: ")

if input_username in usernames:
    print("Access accepted. You can login.")
else:
    print("Access denied.")
