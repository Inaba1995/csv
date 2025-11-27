import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

url = "https://www.divan.ru/sankt-peterburg/category/svet?sort=0"

driver.get(url)

time.sleep(8)

svetilniki = driver.finde_elements(By.CLASS_NAME, 'https://www.divan.ru/sankt-peterburg/category/svet?sort=0')

print(svetilniki)

parsed_data = []

for svetilnik in svetilniki:
   try:

     name = svetilnik.find_element(By.CSS_SELECTOR, '[itemprop="name"]::text').text

     price = svetilnik.find_element(By.CSS_SELECTOR, '[itemprop="price"]::attr(content)').text

     link = svetilnik.find_element(By.CSS_SELECTOR, 'a.bloko-link').get_attribute('href')

   except:
     print("произошла ошибка при парсинге")
         continue

   parsed_data.append([name, price, link])


driver.quit()


with open("divan.csv", 'w', newline='', encoding='utf-8') as file:

    writer = csv.writer(file)

    writer.writerow(['Название', 'Цена', 'ссылка на товар'])

    writer.writerows(parsed_data)

