import math
import time
from selenium import webdriver


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/get_attribute.html"

browser = webdriver.Chrome()
browser.get(link)

x_number = browser.find_element_by_id('treasure').get_attribute('valuex')
answer = calc(x_number)

browser.find_element_by_id('answer').send_keys(answer)
browser.find_element_by_id('robotCheckbox').click()
browser.find_element_by_id('robotsRule').click()
browser.find_element_by_class_name('btn').click()
time.sleep(10)

browser.quit()
