# Import necessary modules
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# Initialize the web driver for Firefox browser
driver = webdriver.Firefox()

# Maximize the browser window
driver.maximize_window()

# Navigate to the URL of the website you want to automate
driver.get("http://127.0.0.1:8000")

# My github credentials
my_username ="admin@gmail.com"
my_password= "admin"

# Access the login username input box
username_input_box = driver.find_element(By.NAME,'username')

# Access the login password input box
password_input_box = driver.find_element(By.NAME,'password')

# Access the login button
login_button = driver.find_element(By.CLASS_NAME,'login__submit')

# Fill in the login credentials
time.sleep(2)
username_input_box.send_keys(my_username)
time.sleep(2)    # 2-second delay between filling username and password
password_input_box.send_keys(my_password)

time.sleep(2)    # 2-second delay

# Click on the login button
login_button.click()

# Wait for the page to load completely
time.sleep(2)

# Fill in the details for the new user
name ="harsh"
ID= "202002088"
password="harsh"
confirm_password="harsh"
Email="harsh@gmail.com"
Courses="SE"
TAs="Jaineel, meet"
Faculties="Saurabh Tiwari"

# Access the input boxes for the new user's details
new_username = driver.find_element(By.NAME,'name')
new_ID = driver.find_element(By.NAME,'id')
select= Select(driver.find_element(By.NAME,'role'))
new_password = driver.find_element(By.NAME,'enter-password')
new_confirm_password = driver.find_element(By.NAME,'confirm-password')
new_email = driver.find_element(By.NAME,'email')
new_courses = driver.find_element(By.NAME,'courses')
new_TAs = driver.find_element(By.NAME,'tas')
new_Faculties = driver.find_element(By.NAME,'faculties')

# Fill in the details for the new user
time.sleep(2)    # 2-second delay
new_username.send_keys(name)

time.sleep(2)    # 2-second delay
new_ID.send_keys(ID)

# Select the role of the new user from the dropdown list
select.select_by_index(1)

time.sleep(2)    # 2-second delay
new_password.send_keys(password)

time.sleep(2)    # 2-second delay
new_confirm_password.send_keys(confirm_password)

time.sleep(2)    # 2-second delay
new_email.send_keys(Email)

time.sleep(2)    # 2-second delay
new_courses.send_keys(Courses)

time.sleep(2)    # 2-second delay
new_TAs.send_keys(TAs)

time.sleep(2)    # 2-second delay
new_Faculties.send_keys(Faculties)

# Click on the submit button to create the new user
driver.find_element(By.CLASS_NAME,'submit-btn').click()

# Wait for the page to load completely
time.sleep(10)

# Close the browser window
driver.close()

















































