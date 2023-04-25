from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By

# create a new instance of the Firefox browser
driver = webdriver.Firefox()
# maximize the browser window
driver.maximize_window()
# navigate to the URL of the web application to be tested
driver.get("http://127.0.0.1:8000")

# specify the username and password to be used for login
my_username ="202001109@daiict.ac.in"
my_password= "darshan"

# find the username input field and enter the username
username_input_box = driver.find_element(By.NAME,'username')
username_input_box.send_keys(my_username)
time.sleep(2) 

# find the password input field and enter the password
password_input_box = driver.find_element(By.NAME,'password')
password_input_box.send_keys(my_password)
time.sleep(2) 

# find the login button and click it to submit the form
log_in_button = driver.find_element(By.CLASS_NAME,'login__submit')
log_in_button.click()
time.sleep(5)

# toggle between dark theme and light theme 4 times
driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[1]').click()
time.sleep(3)
driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[1]').click()
time.sleep(3)
driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[1]').click()
time.sleep(3)
driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[1]').click()
time.sleep(3)

# close the browser window
driver.close()



















