from selenium import webdriver
from moduls.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By

class SignInPage(BasePage):
    URL = "https://github.com/login"

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(SignInPage.URL)

    def try_login(self, username, password):
        login_elem = self.driver.find_element(By.ID, "login_field")

#       # inputing uncorrect username/email
        login_elem.send_keys("sergiibutenko@mistake.com")
#        time.sleep(3)

#       # finding field for uncorrect password inputing 
        pass_elem = self.driver.find_element(By.ID, "password")
    
#       # inputing uncorrect password
        pass_elem.send_keys("wrong password")
#        time.sleep(3)

        btm_elem = self.driver.find_element(By.NAME, "commit")

        btm_elem.click()
#       time.sleep(3)

    def check_title(self, expected_title):
        return self.driver.title == expected_title
