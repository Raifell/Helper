from selenium import webdriver
import time

driver = webdriver.Edge()
driver.get('https://jsonplaceholder.typicode.com')
time.sleep(5)
driver.quit()

#---[В случае проблем с драйверами - использовать код ниже(Path включен)]---#

from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver = webdriver.Edge(EdgeChromiumDriverManager().install())
driver.get('https://jsonplaceholder.typicode.com')
time.sleep(5)
driver.quit()

# При использовании проверить наличие последних версий библиотек selenium и urllib3
