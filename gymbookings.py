### Gym Booking Automation


# Chromedriver downloaded from [https://chromedriver.storage.googleapis.com/index.html?path=91.0.4472.101/]
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


# Logging in
browser = webdriver.Chrome(executable_path=r"C:\Users\Andres\MyPythonScripts\chromedriver.exe")
browser.get('https://user.york-sport.com/bookings/ysc')

log_on_element = browser.find_element_by_id("SF_LogOn")
log_on_element.click()

username_element = browser.find_element_by_name("UserName")
username_element.send_keys("abv787")

password_element = browser.find_element_by_name("Password")
password_element.send_keys("Python19x" + "\n")


# Making bookings
sessions_element = browser.find_elements_by_name("searchType")[1]
sessions_element.click()
date_element = WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.ID, 'SearchDate')))

date_element.click()
date_element.clear()
date_element.click()
date_element.send_keys("01/07/2021" + "\n" + "\n")
