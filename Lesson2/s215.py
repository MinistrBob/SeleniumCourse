import math
import time
from selenium import webdriver


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text
    y = calc(x)
    print(x, y)

    el1 = browser.find_element_by_css_selector("#answer")
    el1.send_keys(str(y))

    el2 = browser.find_element_by_css_selector("#robotCheckbox")
    el2.click()

    el3 = browser.find_element_by_css_selector("#robotsRule")
    el3.click()


    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector(".btn.btn-default")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
