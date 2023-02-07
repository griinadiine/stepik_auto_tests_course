from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Считываем число Х
    x1 = browser.find_element(By.ID, 'input_value')
    x = x1.text
    # Считаем формулу
    y = calc(x)
    # Записываем в поле ответ формулы
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    # код, который выбирает чекбокс
    option1 = browser.find_element(By.ID, 'robotCheckbox')
    option1.click()

    # Скроллим страницу
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    # код, который выбирает радиокнопку
    option2 = browser.find_element(By.ID, 'robotsRule')
    option2.click()
    # Отправляем данные
    button.click()

    # ждем загрузки страницы
    time.sleep(3)

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
