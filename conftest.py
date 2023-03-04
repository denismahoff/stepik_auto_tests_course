import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope="session")
def test_links():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    # url
    browser.get('https://stepik.org/lesson/236895/step/1')

    # choice login
    browser.find_element(By.ID, 'ember33').click()

    # Login to stepik
    browser.find_element(By.ID, 'id_login_email').send_keys('bogmyti88@mail.ru')
    browser.find_element(By.ID, 'id_login_password').send_keys('Kfr284bys!')
    browser.find_element(By.CLASS_NAME, 'sign-form__btn.button_with-loader').click()
    yield browser
    print("\nquit browser..")
    browser.quit()