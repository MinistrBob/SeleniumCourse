from selenium import webdriver
import time
import math


def calc(x):
    print(x)
    result = str(math.log(abs(12 * math.sin(int(x)))))
    print(result)
    return result


link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome(r"C:\Users\bobrovsky\.wdm\drivers\chromedriver\79.0.3945.36\win32\chromedriver.exe")
    browser.get(link)

    button = browser.find_element_by_css_selector(".btn.btn-primary")
    button.click()

    alert = browser.switch_to.alert
    alert.accept()

    value = browser.find_element_by_css_selector("#input_value")
    text = calc(value.text)

    el1 = browser.find_element_by_css_selector("#answer")
    el1.send_keys(text)

    button = browser.find_element_by_css_selector(".btn.btn-primary")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
