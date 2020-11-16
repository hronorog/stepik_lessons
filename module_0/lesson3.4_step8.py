import os
import time
from selenium import webdriver


current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'lesson3.4_step8.txt')
link = "http://suninjuly.github.io/file_input.html"

browser = webdriver.Chrome()
browser.get(link)

browser.find_element_by_name('firstname').send_keys("Кекс")
browser.find_element_by_name('lastname').send_keys('Фекс')
browser.find_element_by_name('email').send_keys('im@im.com')

browser.find_element_by_name('file').send_keys(file_path)

browser.find_element_by_class_name('btn').click()
time.sleep(10)

browser.quit()
