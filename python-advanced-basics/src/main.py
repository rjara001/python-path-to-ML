from models import User
from utils import validate_email, filter_active_users
from errors import ValidationError

def main() -> None:
    users = [
        User(id=1, name="Alice", email="alice@example.com"),
        User(id=2, name="Bob", email="bob[at]example.com", is_active=False),
        User(id=3, name="Charlie", email="charlie@example.com", age=30),
    ]

    valid_users = []

    for user in users:
        try:
            validate_email(user.email)
            valid_users.append(user)
        except ValidationError as error:
            print(f"Validation error for user {user.name}: {error}")

    active_users = filter_active_users(valid_users)


    for user in active_users:
        print(f"Active user: {user.name}, Email: {user.email}")


if __name__ == "__main__":
    main()

