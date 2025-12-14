from .errors import ValidationError

def validate_email(email):
    if "@" not in email:
        raise ValidationError(f"Invalid email address: {email}")

def filter_active_users(users):
    return [user for user in users if user.is_active]


