import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def add_user(driver, name, email):
    """
    Adds a new user by filling out the form and clicking the submit button.
    """
    driver.find_element(By.ID, "username").send_keys(name)
    driver.find_element(By.ID, "email").send_keys(email)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "submit-btn"))
    ).click()

def edit_user(driver, old_email, new_name, new_email):
    """
    Finds a user by email, clicks the Edit button, and updates the user's data.
    """
    user_divs = driver.find_elements(By.CLASS_NAME, "user")
    for div in user_divs:
        if old_email in div.text:
            WebDriverWait(div, 10).until(
                EC.visibility_of_element_located((By.XPATH, ".//button[contains(text(), 'Edit')]"))
            ).click()
            break

    input_name = driver.find_element(By.ID, "username")
    input_name.clear()
    input_name.send_keys(new_name)

    input_email = driver.find_element(By.ID, "email")
    input_email.clear()
    input_email.send_keys(new_email)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "submit-btn"))
    ).click()

def delete_user(driver, email):
    """
    Finds a user by email and clicks the Delete button.
    """
    user_divs = driver.find_elements(By.CLASS_NAME, "user")
    for div in user_divs:
        if email in div.text:
            div.find_element(By.XPATH, ".//button[contains(text(), 'Delete')]").click()
            break

def user_exists(driver, email):
    """
    Checks if a user with the given email exists on the page.
    Returns True if found, False otherwise.
    """
    users = driver.find_elements(By.CLASS_NAME, "user")
    return any(email in user.text for user in users)