import json


def load_users():
    """Load the list of users from users.json."""
    with open("users.json", "r", encoding="utf-8") as f:
        return json.load(f)


def filter_by_name(users, query):
    """Return users whose name contains the query (case-insensitive)."""
    q = query.strip().lower()
    return [u for u in users if q in u["name"].lower()]


def main():
    users = load_users()
    query = input("Enter name to search: ").strip()
    matches = filter_by_name(users, query)

    if not matches:
        print("No user found.")
        return

    for user in matches:
        print(user)


if __name__ == "__main__":
    main()
