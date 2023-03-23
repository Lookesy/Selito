from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import staleness_of
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import time

#Список ключевых фраз по цене
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
"ЦЕНА ЗАВИСИТ", "Цена может меняться", "цены узнавайте", "количества проживающих", "стоимость узнавайте", "Стоимость зависит",
"Цена зависит", "указана от", "Цены уточн", "цену узнавайте", "стоимость может"]

#Ключевые слова по брони
textsetbron = ["брон", "предо", "депозит"]

#Ключевые слова: месяц, день недели
textsetmonth = ["январ", "февра", "март", "апрел", "май", "мая", "мае", "июн", "июл", "авгус", "сент", "октя",
 "нояб", "декаб", "пн", "вт", "ср", "чт", "пт", "сб", "вс", "понедельник", "вторник", "среда", "четверг", "пятница"]

#Ключевые слова: продажа номеров(неверная цена)
textsetotel = ["местн"]

driver = webdriver.Chrome('chromedriver.exe')
driver.get("https://centiman.avito.ru/service-dataset-collector-frontend/login")

#Аутентификация на сайте. Происходит всегда при запуске программы
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

	elif ans == 3:
		element = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "/html/body/div[1]/main/div/div[2]/div[3]/div[1]/div[12]/div[2]/div[3]")))
		driver.find_element("xpath", "/html/body/div[1]/main/div/div[2]/div[3]/div[1]/div[12]/div[2]/div[3]").click()

		#Нажатие кнопки Готово
		driver.find_element("xpath", "/html/body/div/main/div/div[2]/div[3]/button").click()

	elif ans == 11:
		element = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "/html/body/div/main/div/div[2]/div[3]/div[1]/div[12]/div[2]/div[1]")))
		driver.find_element("xpath", "/html/body/div/main/div/div[2]/div[3]/div[1]/div[12]/div[2]/div[1]").click()

	elif ans == 22:
		element = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "/html/body/div/main/div/div[2]/div[3]/div[1]/div[12]/div[2]/div[2]")))
		driver.find_element("xpath", "/html/body/div/main/div/div[2]/div[3]/div[1]/div[12]/div[2]/div[2]").click()

		#Нажатие кнопки Готово
		driver.find_element("xpath", "/html/body/div/main/div/div[2]/div[3]/button").click()




#Проверка на наличие ключевых фраз
def text_find(textset):
	time.sleep(0.5)
	text1 = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "/html/body/div/main/div/div[2]/div[3]/div[1]/div[8]/pre")))
	text1 = driver.find_element("xpath", "/html/body/div/main/div/div[2]/div[3]/div[1]/div[8]/pre")
	text1 = text1.text.lower()
	for word in textset:
		if text1.find(word.lower()) != -1:
			result = 1
			print(word)
			break
		else:
			result = 2
	if result == 1:
		return 1
	elif result == 2:
		return 2

#Проверка на наличие цены в сообщениях продавца
def price_mess():
	time.sleep(0.5)
	element = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//div[@class='row seller']/div")))
	price = driver.find_element("xpath", "//*[@id='app']/main/div/div[2]/div[3]/div[1]/div[6]/pre")

	element = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//div[@class='row seller']")))
	messages_seller = driver.find_elements("xpath", "//div[@class='row seller']/div")
	price = price.text
	price1 = str(int(price) + 1)
	result = 2
	for message in messages_seller:
		message = message.text.lower()
		if message.find(price) != -1 or message.find(price1) != -1:
			if bron(textsetbron) == 1:
				result = 1
				break
		elif message.find("занят") != -1:
			result = 3
			break
		else:
			result = 2
	if result == 1:
		print(len(messages_seller))
		print("Цена: " , price)
		print(message)
		return 1
	elif result == 2:
		return 2
	elif result == 3:
		print(message)
		print("price_mess() Квартира занята")
		return 3


#Функция брони для дополнительной проверки во время проверки на цену в сообщениях продавца
def bron(textsetbron):
	time.sleep(0.5)
	element = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//div[@class='row seller']")))
	messages_seller = driver.find_elements("xpath", "//div[@class='row seller']/div")
	text1 = driver.find_element("xpath", "/html/body/div/main/div/div[2]/div[3]/div[1]/div[8]/pre")
	text1 = text1.text.lower()
	for word in textsetbron:
		for message in messages_seller:
			message = message.text.lower()
			if message.find(word.lower()) != -1:
				print("Сообщение продавца bron(): ", message)
				for word in textsetbron:
					if text1.find(word.lower()) != -1:
						print("Слово, найденное в цикле bron(): ", word)
						return 1
				print("В чате есть бронь, в описании нет")
				return 2
	print("bron() не нашло")
	return 1

#Самостоятельная функция брони, которая в случае обмана со стороны продавца ставит ответ НЕТ
def bron2(textsetbron):
	time.sleep(0.5)
	element = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//div[@class='row seller']")))
	messages_seller = driver.find_elements("xpath", "//div[@class='row seller']/div")
	text1 = driver.find_element("xpath", "/html/body/div/main/div/div[2]/div[3]/div[1]/div[8]/pre")
	text1 = text1.text
	for word in textsetbron:
		for message in messages_seller:
			message = message.text
			if message.find(word) != -1:
				print("Сообщение продавца bron2(): ", message)
				for word in textsetbron:
					if text1.find(word) != -1:
						print("Слово, найденное в цикле bron2(): ", word)
						return 11
				print("В чате есть бронь, в описании нет")
				return 22
	print("bron2() не нашло")
	return 11


def price_month(textsetmonth):
	time.sleep(0.5)
	text1 = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "/html/body/div/main/div/div[2]/div[3]/div[1]/div[8]/pre")))
	text1 = driver.find_element("xpath", "/html/body/div/main/div/div[2]/div[3]/div[1]/div[8]/pre")
	text1 = text1.text.lower()
	element = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//div[@class='row seller']")))
	messages_seller = driver.find_elements("xpath", "//div[@class='row seller']/div")
	for word in textsetmonth:
		word = word.lower()
		if text1.find(word) == -1:
			result = 2
		elif text1.find(word) != -1:
			for message in messages_seller:
				message = message.text.lower()
				if message.find(word):
					result = 1
	if result == 2:
		print("В описании нет периода")
		return 2
	elif result == 1:
		print(word)
		print(message)
		return 1
	else:
		return 11


def check_hotel(textsetotel):
	time.sleep(0.5)
	element = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//div[@class='row seller']")))
	messages_seller = driver.find_elements("xpath", "//div[@class='row seller']/div")
	for message in messages_seller:
		message = message.text.lower()
		for word in textsetotel:
			word = word.lower()
			if message.find(word.lower()) != -1:
				return 3
	return 2

#Запуск действий

#Авторизация
aut()

#Цикл проверок
while True:
	time.sleep(2)
	print("------------")
	if check_hotel(textsetotel)==3:
		print("Неверная цена, продаются номера")
		ansclick(3)
		continue
	if check_hotel(textsetotel)==2:
		ansclick(2)
	if text_find(textset)==1:
		text_find(textset)
		ansclick(1)
		continue
	if text_find(textset)==2:
		print("text_find() Ничего не нашло")
		ansclick(2)
	if price_mess()==1:
		price_mess()
		ansclick(1)
		continue
	if price_mess()==2:
		print("price_mess() Ничего не нашло")
		ansclick(2)
	if price_mess()==3:
		print("price_mess() Занято")
		ansclick(3)
		continue

	#Проверка на бронь в описании и сообщениях продавца(если продавец говорит про бронь/предоплату, а в описании пусто, то ответ нет)
	ansclick(bron2(textsetbron))

	if price_month(textsetmonth)==2:
		print("Цена не верная")
		ansclick(22)
		continue
	if price_month(textsetmonth)==1:
		print("В описании есть период, в чате тоже")
		ansclick(1)
		continue
	if price_month(textsetmonth)==11:
		ansclick(11)



	element = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "/html/body/div/main/div/div[2]/div[3]/div[1]/div[8]/pre")))
	description_next = driver.find_element("xpath", "/html/body/div/main/div/div[2]/div[3]/div[1]/div[8]/pre")

	#Проверка на следующий чат
	while True:

		time.sleep(5)

		#Сравенение описаний сейчас и 2 секунды назад
		description_pred = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "/html/body/div/main/div/div[2]/div[3]/div[1]/div[8]/pre")))
		description_pred = driver.find_element("xpath", "/html/body/div/main/div/div[2]/div[3]/div[1]/div[8]/pre")

		#Если описания разные, то опять запускаются проверки
		if description_pred != description_next:
			break

