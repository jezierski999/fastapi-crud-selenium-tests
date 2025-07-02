import os
import sys
import uuid
from fastapi.testclient import TestClient
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from main import app

# from backend.main import app
client = TestClient(app)

def test_create_valid_user():
    unique_email = f"test_{uuid.uuid4().hex}@example.com"
    response = client.post("/users/", json={
        "name": "Test123",
        "email": unique_email
    })
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Test123"
    assert data["email"] == unique_email

    # Clean-up: delete the user
    user_id = data["id"]
    delete_resp = client.delete(f"/users/{user_id}")
    assert delete_resp.status_code == 200

def test_create_user_invalid_email():
    response = client.post("/users/", json={
        "name": "Test123",
        "email": "not-an-email"
    })
    assert response.status_code == 422
    assert "value is not a valid email address" in response.text

def test_create_user_short_name():
    response = client.post("/users/", json={
        "name": "Te",
        "email": "test@example.com"
    })
    assert response.status_code == 422
    assert "Username must be at least 3 characters long" in response.text

def test_create_user_invalid_chars():
    response = client.post("/users/", json={
        "name": "T@st!",
        "email": "test@example.com"
    })
    assert response.status_code == 422
    assert "Username must contain only letters and digits" in response.text

def test_update_user():
    # Create user
    original_email = f"test_{uuid.uuid4().hex}@example.com"
    create_resp = client.post("/users/", json={
        "name": "OldName",
        "email": original_email
    })
    assert create_resp.status_code == 200
    user_data = create_resp.json()
    user_id = user_data["id"]

    # Update user
    updated_email = f"updated_{uuid.uuid4().hex}@example.com"
    update_resp = client.put(f"/users/{user_id}", json={
        "name": "NewName",
        "email": updated_email
    })
    assert update_resp.status_code == 200
    updated_user = update_resp.json()

    # Validate updated data
    assert updated_user["name"] == "NewName"
    assert updated_user["email"] == updated_email
    assert updated_user["id"] == user_id

    # Clean-up: delete updated user
    delete_resp = client.delete(f"/users/{user_id}")
    assert delete_resp.status_code == 200
