from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators:
    LOGIN_EMAIL_LINK = (By.CSS_SELECTOR, '[name="login-username"]')
    LOGIN_PSD_LINK = (By.CSS_SELECTOR, '[name="login-password"]')
    LOGIN_BTN = (By.CSS_SELECTOR, 'name="login_submit"]')

    REGISTRATION_EMAIL_LINK = (By.CSS_SELECTOR, '[name="registration-email"]')
    REGISTRATION_PSD_LINK = (By.CSS_SELECTOR, '[name="registration-password1"]')
    REGISTRATION_PSD_REPEAT_LINK = (By.CSS_SELECTOR, '[name="registration-password2"]')
    REGISTRATION_BTN = (By.CSS_SELECTOR, '[name="registration_submit"]')
