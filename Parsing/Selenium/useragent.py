from selenium import webdriver
import time

url = 'https://www.whatismybrowser.com/detect/what-is-my-user-agent'

options = webdriver.EdgeOptions() # Объект опций
options.add_argument('user-agent=HelloWorld:)')

driver = webdriver.Edge(options=options)

try:
    driver.get(url=url)
    time.sleep(10)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()


