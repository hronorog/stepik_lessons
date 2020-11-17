import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestRegistration(unittest.TestCase):
    def test1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        browser.find_element(By.CSS_SELECTOR, '.first_block .first').send_keys('Иван')
        browser.find_element(By.CSS_SELECTOR, '.first_block .second').send_keys('Петров')
        browser.find_element(By.CSS_SELECTOR, '.first_block .third').send_keys('im@mail.com')

        browser.find_element_by_css_selector("button.btn").click()
        welcome_text = browser.find_element_by_tag_name("h1").text
        welcome_expected = "Congratulations! You have successfully registered!"

        self.assertEqual(welcome_expected, welcome_text, "Successfull test!")

    def test2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        browser.find_element(By.CSS_SELECTOR, '.first_block .first').send_keys('Иван')
        browser.find_element(By.CSS_SELECTOR, '.first_block .second').send_keys('Петров')
        browser.find_element(By.CSS_SELECTOR, '.first_block .third').send_keys('im@mail.com')

        browser.find_element_by_css_selector("button.btn").click()
        welcome_text = browser.find_element_by_tag_name("h1").text
        welcome_expected = "Congratulations! You have successfully registered!"

        self.assertEqual(welcome_expected, welcome_text, "Successfull test!")


if __name__ == '__main__':
    unittest.main()


