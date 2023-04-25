
# import necessary libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By

# create a Firefox webdriver instance
driver = webdriver.Firefox()

# maximize the browser window
driver.maximize_window()

# navigate to the website to be automated
driver.get("http://127.0.0.1:8000")

# specify credentials to login
my_username ="admin@gmail.com"
my_password= "admin"

# locate the login username input element
username_input_box = driver.find_element(By.NAME,'username')

# locate the login password input element
password_input_box = driver.find_element(By.NAME,'password')

# locate the login button element
log_in_button = driver.find_element(By.CLASS_NAME,'login__submit')

# clear the input boxes to remove any pre-populated data
# username_input_box.clear()
# password_input_box.clear()

# fill in the login credentials
time.sleep(2)
username_input_box.send_keys(my_username)
time.sleep(2)    #2 second time gap between filling username and password
password_input_box.send_keys(my_password)

time.sleep(2)    #2 second time delay

# click the login button to submit the login credentials
log_in_button.click()

time.sleep(5)

# navigate to the leave status pending page
driver.find_element(By.XPATH,'//a[contains(@href,"leave_status_pending")]').click()
time.sleep(5)

# navigate to the student data page
driver.find_element(By.XPATH,'//a[contains(@href,"student_data")]').click()
time.sleep(5)

# navigate to the faculty data page
driver.find_element(By.XPATH,'//a[contains(@href,"faculty_data")]').click()
time.sleep(5)

# navigate to the TA data page
driver.find_element(By.XPATH,'//a[contains(@href,"ta_data")]').click()
time.sleep(30)

# close the browser window
driver.close()

















