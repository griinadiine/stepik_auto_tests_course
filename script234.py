from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Нажимаем на кнопку
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Принимаем confirm
    confirm = browser.switch_to.alert
    confirm.accept()

    # ждем загрузки страницы
    time.sleep(1)

    # Считываем число Х
    x1 = browser.find_element(By.ID, 'input_value')
    x = x1.text
    # Считаем формулу
    y = calc(x)

    # Записываем в поле ответ формулы
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)

    # Отправляем данные
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
