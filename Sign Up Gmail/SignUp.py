from selenium import webdriver
from selenium.webdriver.common.by import By

# Launch the browser and navigate to the sign-up page
browser = webdriver.Edge()
browser.get("https://accounts.google.com/signup/v2/webcreateaccount?service=accountsettings&continue=https%3A%2F%2Fmyaccount.google.com%2F&hl=en&biz=false&flowName=GlifWebSignIn&flowEntry=SignUp")
assert "Create your Google Account" in browser.title

# Enter the information
fName_input = browser.find_element(By.ID, "firstName")
lName_input = browser.find_element(By.NAME, "lastName")
email_input = browser.find_element(By.ID, "username")
password_input = browser.find_element(By.NAME, "Passwd")
confirm_password_input = browser.find_element(By.NAME, "ConfirmPasswd")
fName_input.send_keys("Tester Samantha")
lName_input.send_keys("Indonesia")
email_input.send_keys("testersamanthaindo.com")
password_input.send_keys("samantha@2023")
confirm_password_input.send_keys("samantha@2023")

# Next
next_link = browser.find_element(By.ID, "accountDetailsNext")
next_link.click()

# Close the browser
browser.quit()
