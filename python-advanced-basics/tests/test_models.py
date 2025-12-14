from src.advanced_basic.models import User

def test_user_creation():
    user = User(id=1, name="testuser", email="testuser@example.com")
    assert user.name == "testuser"
    assert user.email == "testuser@example.com"
    assert user.is_active is True

