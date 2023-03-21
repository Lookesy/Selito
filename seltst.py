from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import staleness_of
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import time

textset = ["цена зависит", "цену уточняйте", "цены зависят", "стоимость зависит", "цена варьируется",
"стоимость варьируется", "на стоимость влияет", "на стоимость влияют", "на цену влияет",
"на цену влияют", "от сезона", "от количества проживающих", "стоимость может меняться", "зависит от срока проживания",
"сезона", "СТОИМОСТЬ АРЕНДЫ ЗАВИСИТ", "окончательную стоимость", "стоимость уточняйте", "ЦЕНУ уточняйте", "Стоимость проживания зависит", "Уточняйте стоимость",
"Цена меняется, в зависимости от", "чем больше дней, тем меньше цена", "Цена может меняться", "Стоимость зависит", "Стоимость выше указана минимальная", 
"стоимость выше указана минимальная", "Цену уточнять", "цену уточнять", "ценах, свободных датах пожалуйста уточняйте",
"цены, свободные даты пожалуйста уточняйте", "стоимость проживания зависит", "Цена зависит",
"Цены уточняйте", "Цена в объявлении может меняться", "Стоимость зависит", "Стоимость может меняться",
"Цена может варьироваться", "Цена варьируется", "Цену уточнять", "цену уточнять", "Цена договорная", "цена договорная",
"Цена может меняться", "Цена меняется", "Стоимость проживания зависит", "Цены и конкретные даты уточняйте",
"Цену уточняйте", "количеcтва человeк", "стоимость и наличие свободной квартиры уточняйте", "Цен может отличаться",
"Ценa зависит", "зависит от", "ЦЕНА зависит", "Цена аренды квартиры может", "В зависимости от", "в зависимости от",
"Чтобы узнать стоимость", "Стоимость указана на текущие дни", "Актуальную стоимость", "актуальную стоимость", "уточняйте", "Уточняйте цены",
"ЦЕНА ЗАВИСИТ", "Цена может меняться"]

driver = webdriver.Chrome('chromedriver.exe')
driver.get("https://centiman.avito.ru/service-dataset-collector-frontend/login")

def aut():
	login = "dtitov"
	password = "evwaaAqRVwZd"

	element = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//input[@type='text']")))
	driver.find_element("xpath", "//input[@type='text']").send_keys(login)
	driver.find_element("xpath", "//input[@type='password']").send_keys(password)

	driver.find_element("xpath", "//div[@class='button']").click()

	element = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//*[@id='app']/main/div/div/div/div/a")))
	driver.find_element("xpath", "//*[@id='app']/main/div/div/div/div/a").click()

	time.sleep(2)

def ansclick(ans):
	if ans == 1:
		element = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "/html/body/div/main/div/div[2]/div[3]/div[1]/div[12]/div[2]/div[1]")))
		driver.find_element("xpath", "/html/body/div/main/div/div[2]/div[3]/div[1]/div[12]/div[2]/div[1]").click()

		#Нажатие кнопки Готово
		driver.find_element("xpath", "/html/body/div/main/div/div[2]/div[3]/button").click()
	elif ans == 2:
		element = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "/html/body/div/main/div/div[2]/div[3]/div[1]/div[12]/div[2]/div[2]")))
		driver.find_element("xpath", "/html/body/div/main/div/div[2]/div[3]/div[1]/div[12]/div[2]/div[2]").click()


def text_find(textset):
	element = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "/html/body/div/main/div/div[2]/div[3]/div[1]/div[8]/pre")))
	text1 = driver.find_element("xpath", "/html/body/div/main/div/div[2]/div[3]/div[1]/div[8]/pre")
	text1 = text1.text
	for word in textset:
		if text1.find(word) != -1:
			result = 1
			break
		else:
			result = 2
	if result == 1:
		ansclick(1)
	elif result == 2:
		ansclick(2)


def price_mess():
	time.sleep(1)
	element = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//div[@class='row seller']/div")))
	price = driver.find_element("xpath", "//*[@id='app']/main/div/div[2]/div[3]/div[1]/div[6]/pre")

	element = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//div[@class='row seller']")))
	messages_seller = driver.find_elements("xpath", "//div[@class='row seller']/div")
	price = price.text
	price1 = str(int(price) + 1)
	print(len(messages_seller))
	for message in messages_seller:
		message = message.text
		if message.find(price) != -1 or message.find(price1) != -1:
			result =1
			break
		else:
			result = 2
	if result == 1:
		ansclick(1)
	elif result == 2:
		ansclick(2)


#Запуск действий

#Авторизация
aut()

#Цикл проверок
while True:
	text_find(textset)

	price_mess()

	while True:
		
		element = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "/html/body/div/main/div/div[2]/div[3]/div[1]/div[8]/pre")))
		description_pred = driver.find_element("xpath", "/html/body/div/main/div/div[2]/div[3]/div[1]/div[8]/pre")

		time.sleep(2)

		element = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "/html/body/div/main/div/div[2]/div[3]/div[1]/div[8]/pre")))
		description_next = driver.find_element("xpath", "/html/body/div/main/div/div[2]/div[3]/div[1]/div[8]/pre")

		if description_pred != description_next:
			break

