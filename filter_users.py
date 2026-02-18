import json


def load_users():
    """Load the list of users from users.json."""
    with open("users.json", "r", encoding="utf-8") as f:
        return json.load(f)


def filter_by_name(users, query):
    """Return users whose name contains the query (case-insensitive)."""
    q = query.strip().lower()
    return [u for u in users if q in u["name"].lower()]

def filter_by_age(users, min_age):
    """Return users whose age is greater or equal to min_age."""
    return [u for u in users if u["age"] >= min_age]

def filter_by_email(users, query):
    """Return users whose email contains the query (case-insensitive)."""
    q = query.strip().lower()
    return [u for u in users if q in u["email"].lower()]


def main():
    users = load_users()
    choice = input("Filter by (1) name, (2) age, or (3) email? ").strip()

    if choice == "1":
        query = input("Enter name to search: ").strip()
        matches = filter_by_name(users, query)

    elif choice == "2":
        min_age = int(input("Enter minimum age: ").strip())
        matches = filter_by_age(users, min_age)

    elif choice == "3":
        query = input("Enter email text to search: ").strip()
        matches = filter_by_email(users, query)


    else:
        print("Invalid choice.")
        return

    if not matches:
        print("No user found.")
        return

    for user in matches:
        print(user)


if __name__ == "__main__":
    main()
