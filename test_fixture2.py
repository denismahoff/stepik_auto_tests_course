import pytest
import time
import math

answer = math.log(int(time.time()))
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://stepik.org/lesson/236895/step/1"


@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    return browser


class TestloginPage1:
    # вызываем фикстуру в тесте, передав ее как параметр
    def test_login_link1(self, browser):
        browser = webdriver.Chrome()

        # wait

        browser.implicitly_wait(15)

        # url
        browser.get(link)

        # choice login
        browser.find_element(By.ID, 'ember33').click()

        # Login to stepik
        browser.find_element(By.ID, 'id_login_email').send_keys('bogmyti88@mail.ru')
        browser.find_element(By.ID, 'id_login_password').send_keys('Kfr284bys!')
        browser.find_element(By.CLASS_NAME, 'sign-form__btn.button_with-loader').click()

        # write answer
        browser.find_element(By.CLASS_NAME, 'ember-text-area.ember-view.textarea.string-quiz__textarea').send_keys(
            answer)

        # send answer
        button = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'submit-submission'))
        )
        button.click()
