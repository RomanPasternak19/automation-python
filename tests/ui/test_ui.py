import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

@pytest.mark.ui
def test_check_incorrect_username():
    driver = webdriver.Chrome(
        service=Service(r"/home/roman/Desktop/automation/automation-python/chromedriver-linux64" + r"/chromedriver")
    )

    driver.get("https://github.com/login")

    login_element = driver.find_element(By.ID, 'login_field')
    login_element.send_keys("roman.pasternak19@mistakeemail.com")
    
    pass_element = driver.find_element(By.ID, 'password')
    pass_element.send_keys('wrong password')

    btn_elem = driver.find_element(By.NAME, 'commit')
    btn_elem.click()

    assert driver.title == 'Sign in to GitHub · GitHub'
    time.sleep(3)

    driver.close()