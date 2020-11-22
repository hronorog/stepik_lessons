from random import sample
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


link = "http://selenium1py.pythonanywhere.com/ru/"
account_email = '{}@mail.ru'.format("".join(sample("abcdefjhig", 10)))  # генерация рандомного имени почты из 10 символов
account_pswd = "123456789Zz!"
selector_login_button = "[id='login_link']"
selector_email = "[name='registration-email']"
selector_pswd = "[name='registration-password1']"
selector_pswd_rpt = "[name='registration-password2']"
selector_reg_button = "[value='Register']"


def test_registration_new_account():
    """
    Тестовый сценарий 1.1.1 Регистрация нового пользователя
    """
    success_locator = "//div[@class='alertinner wicon']"
    success_message = "Спасибо за регистрацию!"
    try:
        # Arrange
        browser = webdriver.Chrome()
        browser.implicitly_wait(10)
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, selector_login_button).click()

        email = browser.find_element(By.CSS_SELECTOR, selector_email)
        email.send_keys(account_email)

        password = browser.find_element(By.CSS_SELECTOR, selector_pswd)
        password.send_keys(account_pswd)

        password_repeat = browser.find_element(By.CSS_SELECTOR, selector_pswd_rpt)
        password_repeat.send_keys(account_pswd)

        # Act
        registration_button = browser.find_element(By.CSS_SELECTOR, selector_reg_button)
        registration_button.click()

        # Assert
        login_success = browser.find_element(By.XPATH, success_locator)
        assert success_message in login_success.text, "Registration failed."
    finally:
        time.sleep(5)
        browser.quit()


if __name__ == "__main__":
    test_registration_new_account()
