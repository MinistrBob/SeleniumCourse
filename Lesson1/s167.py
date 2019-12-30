from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements_by_css_selector('input[type="text"]')
    for element in elements:
        element.send_keys("sss")

    button = browser.find_element_by_css_selector(".btn.btn-default")
    button.click()

    alert = browser.switch_to.alert
    print(alert.text.split()[-1])
    alert.accept()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
