from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select



driver = webdriver.Firefox()
driver.maximize_window()
driver.get("http://127.0.0.1:8000")

# Create an instance of Firefox browser, maximize window and open the given URL

# My GitHub credentials
my_username = "202001109@daiict.ac.in"
my_password = "darshan"

# Access login username input
username_input_box = driver.find_element(By.NAME, 'username')

# Access login password input
password_input_box = driver.find_element(By.NAME, 'password')

# Access login button
log_in_button = driver.find_element(By.CLASS_NAME, 'login__submit')

# Fill login credentials

username_input_box.send_keys(my_username)  # Filling username
time.sleep(2)  # Adding a 2 second delay
password_input_box.send_keys(my_password)  # Filling password

time.sleep(2)

# Click on login button
log_in_button.click()

time.sleep(4)

# Click on a link with a partial URL containing "profile_page"
driver.find_element(By.XPATH, '//a[contains(@href,"profile_page")]').click()

time.sleep(4)

# Click on a button with ID 'button3'
driver.find_element(By.ID, 'button3').click()

time.sleep(3)

# Select a dropdown option by index
select = Select(driver.find_element(By.NAME, 'leave-type'))
select.select_by_index(1)

time.sleep(3)

# Fill the 'from-date' field
from_date = driver.find_element(By.XPATH, '//*[@id="from-date"]')
from_date.send_keys("2023-04-26")

time.sleep(3)

# Fill the 'to-date' field
to_date = driver.find_element(By.XPATH, '//*[@id="to-date"]')
to_date.send_keys("2023-04-27")

time.sleep(3)

# Fill the reason text box
reason = driver.find_element(By.CLASS_NAME, 'reason-text')
reason.send_keys("IT314-Software Engineering")

time.sleep(3)

# Click on a button with class name 'submit-btn'
driver.find_element(By.CLASS_NAME, 'submit-btn').click()

time.sleep(7)

























