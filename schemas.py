from pydantic import BaseModel, EmailStr, field_validator, ConfigDict
import re

class User(BaseModel):
    """
    Schema representing the input for creating or updating a user.
    Includes name and email validation.
    """
    name: str
    email: EmailStr

    @field_validator("name")
    @classmethod
    def validate_name(cls, value: str) -> str:
        """
        Validates the 'name' field:
        - Minimum length: 3 characters
        - Maximum length: 20 characters
        - Only letters and digits are allowed
        """
        if len(value) < 3:
            raise ValueError("Username must be at least 3 characters long")
        if len(value) > 20:
            raise ValueError("Username must be at most 20 characters long")
        if not re.match(r"^[a-zA-Z0-9]+$", value):
            raise ValueError("Username must contain only letters and digits")
        return value

class UserInDB(User):
    """
    Schema representing a user stored in the database.
    Includes the user's ID.
    """
    id: int

    model_config = ConfigDict(from_attributes=True)  # Enables ORM compatibility