from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/registration1.html"    # test success
# link = "http://suninjuly.github.io/registration2.html"  # test invalid

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # xpath
    # browser.find_element(By.XPATH, '//div[@class="first_block"]//input[@class="form-control first"]').send_keys('Иван')
    # browser.find_element(By.XPATH, '//div[@class="first_block"]//input[@class="form-control second"]').send_keys('Петров')
    # browser.find_element(By.XPATH, '//div[@class="first_block"]//input[@class="form-control third"]').send_keys('im@mail.com')

    # css
    browser.find_element(By.CSS_SELECTOR, '.first_block .first').send_keys('Иван')
    browser.find_element(By.CSS_SELECTOR, '.first_block .second').send_keys('Петров')
    browser.find_element(By.CSS_SELECTOR, '.first_block .third').send_keys('im@mail.com')

    browser.find_element_by_css_selector("button.btn").click()
    time.sleep(1)

    # находим элемент, содержащий текст, записываем текст
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = browser.find_element_by_tag_name("h1").text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
