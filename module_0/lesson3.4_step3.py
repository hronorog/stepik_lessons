import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select


link = "http://suninjuly.github.io/selects1.html"

browser = webdriver.Chrome()
browser.get(link)

num_1 = browser.find_element_by_id('num1').text
num_2 = browser.find_element_by_id('num2').text

Select(browser.find_element_by_id('dropdown')).select_by_visible_text(str(int(num_1) + int(num_2)))
browser.find_element_by_class_name('btn').click()
time.sleep(10)

browser.quit()
