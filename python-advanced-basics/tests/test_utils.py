import pytest
from src.advanced_basic.errors import ValidationError
from src.advanced_basic.utils import validate_email

def test_validate_email_success():
    validate_email("rjara@gmail.com")  # Si no lanza, el test pasa

def test_validate_email_failure():
    # Debe lanzar ValidationError
    with pytest.raises(ValidationError):
        validate_email("invalido")