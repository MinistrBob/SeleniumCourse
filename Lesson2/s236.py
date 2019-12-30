from selenium import webdriver
import time
import math
import re


def calc(x):
    print(x)
    result = str(math.log(abs(12 * math.sin(int(x)))))
    print(result)
    return result


link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome(r"C:\Users\bobrovsky\.wdm\drivers\chromedriver\79.0.3945.36\win32\chromedriver.exe")
    browser.get(link)

    button = browser.find_element_by_css_selector(".trollface.btn.btn-primary")
    button.click()

    windows = browser.window_handles
    current_window = browser.current_window_handle

    for win in windows:
        if current_window == win:
            print(win, " with current index: ", windows.index(win))
        else:
            print(win, " with index: ", windows.index(win))

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    value = browser.find_element_by_css_selector("#input_value")
    text = calc(value.text)

    el1 = browser.find_element_by_css_selector("#answer")
    el1.send_keys(text)

    button = browser.find_element_by_css_selector(".btn.btn-primary")
    button.click()

    alert = browser.switch_to.alert
    alert_text = alert.text
    text = re.findall("(?:Congrats, you've passed the task! Copy this code as the answer to Stepik quiz:\s)(.*)",
                      alert_text)
    print(text)


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
