from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
import numpy as np

service = Service('chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.implicitly_wait(15) 
driver.get('https://www.delivery-club.ru/srv/red_drakon_tvjer_vd')

list_products = driver.find_elements(By.XPATH, "//div[@class='menu-product__title']")
list_products_rolls = []
for pizza in list_products:
    if pizza.text.__contains__('лососем'):
        list_products_rolls.append(pizza)

random_num = np.random.randint(0,len(list_products_rolls))
actions = ActionChains(driver)
actions.move_to_element(list_products_rolls[random_num])
actions.perform()
button_basket = driver.find_element(By.XPATH, "//button[contains(@class, 'menu-product__btn--hover')]")
button_basket.click()

print("Можете ввести адрес")
