from selenium import webdriver
import time

url1 = 'https://instagram.com/'
url2 = 'https://stackoverflow.com/'
driver = webdriver.Edge()

try:
    driver.get(url=url1) # Открывает страницу
    time.sleep(5)
    driver.refresh() # Обновляет страницу
    time.sleep(2)
    driver.get_screenshot_as_file('Temp/1.png') # Сохраняетскрин страницы в файл
    driver.get(url=url2)
    time.sleep(5)
    driver.save_screenshot('Temp/2.png') # Сохраняетскрин страницы в файл
    time.sleep(2)
except Exception as ex:
    print(ex)
finally:
    driver.close() # Закрытие окна
    driver.quit() # Закрытие программы

# Selenium работает только с одним окном браузера
