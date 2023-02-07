import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# import time

# @pytest.mark.ui
# def test_chek_incorrect_username():
#     # creatig object to browser manage
#     driver = webdriver.Chrome(
#         service = Service(r"//////"+"chromedriver.exe")
#     )

#     # opening browser
#     driver.get('https://github.com/login')

#     # finding field for uncorrect name/email inputing
#     login_elem = driver.find_element(By.ID, "login_field")

#     # inputing uncorrect username/email
#     login_elem.send_keys("sergiibutenko@mistake.com")
#     time.sleep(3)

#     # finding field for uncorrect password inputing 
#     pass_elem = driver.find_element(By.ID, "password")
    
#     # inputing uncorrect password
#     pass_elem.send_keys("wrong password")
#     time.sleep(3)

#     btm_elem = driver.find_element(By.NAME, "commit")

#     btm_elem.click()
#     time.sleep(3)

#     assert driver.title == "Sign is to GitHub. GitHub"
#     time.sleep(3)

#     # closing browser
#     driver.close()


# 2 Test sign in on GitHub page by Page Object Models
