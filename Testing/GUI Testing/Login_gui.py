# Import necessary modules from Selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By

# Initialize Firefox webdriver and maximize the window
driver = webdriver.Firefox()
driver.maximize_window()

# Load the website to be accessed
driver.get("http://127.0.0.1:8000")

# Set login credentials
my_username ="admin@gmail.com"
my_password= "admin"

# Find the username input box by its name attribute
username_input_box = driver.find_element(By.NAME,'username')

# Find the password input box by its name attribute
password_input_box = driver.find_element(By.NAME,'password')

# Find the login button by its class name
login_button = driver.find_element(By.CLASS_NAME,'login__submit')

# Clear the placeholders data in the input boxes
# username_input_box.clear()
# password_input_box.clear()

# Fill in the login credentials
time.sleep(2) # Add a 2 second time gap before entering the username
username_input_box.send_keys(my_username)
time.sleep(2) # Add a 2 second time gap before entering the password
password_input_box.send_keys(my_password)

time.sleep(2) # Add a 2 second time gap before clicking the login button

# Click the login button
login_button.click()

time.sleep(2) # Add a 2 second time gap before clicking logout

# Find the logout button by its xpath and click it
driver.find_element(By.XPATH,'//a[contains(@href,"logout")]').click()

time.sleep(3) # Add a 3 second time gap before moving to the next login

# Set the next login credentials
my_username ="202001074@daiict.ac.in"
my_password= "saurabh"

# Find the input boxes and login button again
username_input_box = driver.find_element(By.NAME,'username')
password_input_box = driver.find_element(By.NAME,'password')
login_button = driver.find_element(By.CLASS_NAME,'login__submit')

# Fill in the next login credentials
username_input_box.send_keys(my_username)
time.sleep(2) # Add a 2 second time gap before entering the password
password_input_box.send_keys(my_password)

time.sleep(2) # Add a 2 second time gap before clicking the login button

# Click the login button
login_button.click()

time.sleep(2) # Add a 2 second time gap before clicking logout

# Find the logout button by its xpath and click it
driver.find_element(By.XPATH,'//a[contains(@href,"logout")]').click()

time.sleep(3) # Add a 3 second time gap before moving to the next login

# Set the next login credentials
my_username ="202001088@daiict.ac.in"
my_password= "harsh"

# Find the input boxes and login button again
username_input_box = driver.find_element(By.NAME,'username')
password_input_box = driver.find_element(By.NAME,'password')
login_button = driver.find_element(By.CLASS_NAME,'login__submit')

# Clear the placeholders data in the input boxes
# username_input_box.clear()
# password_input_box.clear()

# Fill in the next login credentials
username_input_box.send_keys(my_username)
time.sleep(2) # Add a 2 second time gap before entering the password
password_input_box.send_keys(my_password)

time.sleep(2) # Add a 2 second time gap before clicking the login button

# Click the login button
login_button.click()

time.sleep(2) # Add a 2 second time gap before clicking logout

driver.find_element(By.XPATH,'//a[contains(@href,"logout")]').click()
# print(logout_button)
time.sleep(3)
# driver.close()
# username_input_box.clear()
# password_input_box.clear()






my_username ="vaidehi@gmail.com"
my_password= "vaideh"

#access login username input
username_input_box = driver.find_element(By.NAME,'username')

#access login password input
password_input_box = driver.find_element(By.NAME,'password')

#access login button
login_button = driver.find_element(By.CLASS_NAME,'login__submit')

#clear the placeholders data
# username_input_box.clear()
# password_input_box.clear()

#fill login credentials
username_input_box.send_keys(my_username)
time.sleep(2)    #2 second time gap between filling username and password
password_input_box.send_keys(my_password)

time.sleep(2)    #2 second time delay

#hit the login button
login_button.click()

time.sleep(2)  
driver.find_element(By.XPATH,'//a[contains(@href,"logout")]').click()
# print(logout_button)
# automatically close the driver after 30 seconds
time.sleep(30)
driver.close()

# username_input_box.clear()
# password_input_box.clear()





















































