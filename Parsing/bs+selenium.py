from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

driver = webdriver.Edge()
driver.get('https://www.accuweather.com/ru/uz/tashkent/351199/weather-forecast/351199')
element = driver.find_element(By.XPATH, '//*')
source = element.get_attribute('outerHTML') # innerHTML

soup = BeautifulSoup(source, 'lxml')
vir1 = soup.find('div', class_='temp-container').find('div', class_='temp').text
vir2 = soup.find('div', class_='cur-con-weather-card__panel details-container')

print(vir1)
print(vir2)
time.sleep(5)

driver.close()
driver.quit()
