from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os.path

pathname = os.path.abspath(os.getcwd())
pathname = pathname + "/chromedriver"
link = raw_input("Amazon link: ")
name = raw_input("Username: ")
ww = raw_input("Password: ")
buyAvailable = "false"

driver = webdriver.Chrome(pathname) 
driver.get(link)

# Check for cookies
try:
    cookies = driver.find_element_by_id("sp-cc-accept")
    cookies.click()
except:
    print("no cookies!")

# While loop if product is not yet available
while buyAvailable == "false":
    try:
        buyNow = driver.find_element_by_id("buy-now-button")
        buyNow.click()
        buyAvailable = "true"
    except: 
        driver.refresh()

# Email
email = driver.find_element_by_id("ap_email")
email.send_keys(name)

# Continue
cn = driver.find_element_by_id("continue")
cn.click()

# Password
passw = driver.find_element_by_id("ap_password")
passw.send_keys(ww)

# Login 
login = driver.find_element_by_id("signInSubmit")
login.click()