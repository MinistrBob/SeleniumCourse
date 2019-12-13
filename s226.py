import math
import time
from selenium import webdriver


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text
    y = calc(x)
    print(x, y)

    el1 = browser.find_element_by_css_selector("#answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", el1)
    el1.send_keys(str(y))

    el2 = browser.find_element_by_css_selector("#robotCheckbox")
    browser.execute_script("return arguments[0].scrollIntoView(true);", el2)
    el2.click()

    el3 = browser.find_element_by_css_selector("#robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", el3)
    el3.click()

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector(".btn.btn-primary")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
