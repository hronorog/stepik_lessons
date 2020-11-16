import math
import time
from selenium import webdriver


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/execute_script.html"

browser = webdriver.Chrome()
browser.get(link)

x_number = browser.find_element_by_id('input_value').text
answer = calc(x_number)

browser.find_element_by_id('answer').send_keys(answer)
browser.find_element_by_id('robotCheckbox').click()

button = browser.find_element_by_id("robotsRule")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)  # прокрутка страницы до видимости элемента
button.click()

browser.find_element_by_class_name('btn').click()
time.sleep(10)

browser.quit()
