import math
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    el1 = browser.find_element_by_css_selector("#num1")
    num1 = el1.text
    el2 = browser.find_element_by_css_selector("#num2")
    num2 = el2.text
    sum_ = str(int(num1) + int(num2))

    select = Select(browser.find_element_by_tag_name("#dropdown"))
    select.select_by_value(sum_)  # ищем элемент с текстом "Python"

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector(".btn.btn-default")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
