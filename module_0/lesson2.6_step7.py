from selenium import webdriver
import time


link = "http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_tag_name("input").send_keys("Ivan")
    browser.find_element_by_name("last_name").send_keys("Petrov")
    browser.find_element_by_class_name("city").send_keys("Smolensk")
    browser.find_element_by_id("country").send_keys("Russia")
    browser.find_element_by_xpath("//button[text()='Submit']").click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
