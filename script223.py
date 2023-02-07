from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try: 
    link = "https://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Получаем первое число
    x = browser.find_element(By.ID, 'num1')
    x1 = x.text
    # Получаем второе число
    y = browser.find_element(By.ID, 'num2')
    y1 = y.text
    # Считаем сумму чисел
    s = int(x1) + int(y1)

    # Находим список
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    # Находим значение равное сумме цифр
    select.select_by_value(str(s)) 

    # Отправляем данные
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # ждем загрузки страницы
    time.sleep(3)

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
