import math
import time
from selenium import webdriver


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/alert_accept.html"

browser = webdriver.Chrome()
browser.get(link)

browser.find_element_by_tag_name('button').click()
browser.switch_to.alert.accept()

x_number = browser.find_element_by_id('input_value').text
answer = calc(x_number)

browser.find_element_by_id('answer').send_keys(answer)
browser.find_element_by_class_name('btn').click()

sign = browser.switch_to.alert
print(sign.text.split()[-1])
sign.accept()
time.sleep(5)

browser.quit()
