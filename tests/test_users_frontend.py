import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from tests.utils import add_user, edit_user, delete_user, user_exists
import uuid


def test_add_edit_delete_user(driver):
    """End-to-end test for adding, editing, and deleting a user on the frontend UI."""

    # Generate unique emails for test isolation
    email = f"test_{uuid.uuid4().hex[:8]}@example.com"
    new_email = f"new_{uuid.uuid4().hex[:8]}@example.com"

    # Add user
    add_user(driver, "TestUser", email)
    assert user_exists(driver, email), "User was not added successfully"

    # Edit user
    edit_user(driver, email, "UpdatedUser", new_email)
    assert user_exists(driver, new_email), "User was not updated successfully"
    assert not user_exists(driver, email), "Old email is still present after update"

    # Delete user
    delete_user(driver, new_email)
    assert not user_exists(driver, new_email), "User was not deleted successfully"
