from selenium import webdriver
import time

textset = ["цена зависит", "цену уточняйте", "цены зависят", "стоимость зависит", "цена варьируется",
"стоимость варьируется", "на стоимость влияет", "на стоимость влияют", "на цену влияет",
"на цену влияют", "от сезона", "от количества проживающих", "стоимость может меняться", "зависит от срока проживания",
"сезона", "СТОИМОСТЬ АРЕНДЫ ЗАВИСИТ", "окончательную стоимость"]

driver = webdriver.Chrome('chromedriver.exe')
driver.get("https://centiman.avito.ru/service-dataset-collector-frontend/login")

def aut():
	login = "dtitov"
	password = "evwaaAqRVwZd"

	driver.find_element("xpath", "//input[@type='text']").send_keys(login)
	driver.find_element("xpath", "//input[@type='password']").send_keys(password)

	driver.find_element("xpath", "//div[@class='button']").click()

	time.sleep(2)

	driver.find_element("xpath", "//*[@id='app']/main/div/div/div/div/a").click()

	time.sleep(2)

def ansclick(ans):
	if ans == 1:
		driver.find_element("xpath", "/html/body/div/main/div/div[2]/div[3]/div[1]/div[12]/div[2]/div[1]").click()

		#Нажатие кнопки Готово
		driver.find_element("xpath", "/html/body/div/main/div/div[2]/div[3]/button").click()
	elif ans == 2:
		driver.find_element("xpath", "/html/body/div/main/div/div[2]/div[3]/div[1]/div[12]/div[2]/div[2]").click()


def text_find(textset):
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

#Запуск действий

#Авторизация
aut()

#Цикл проверок
while True:
	text_find(textset)

	while True:
		
		description_pred = driver.find_element("xpath", "/html/body/div/main/div/div[2]/div[3]/div[1]/div[8]/pre")

		time.sleep(2)

		description_next = driver.find_element("xpath", "/html/body/div/main/div/div[2]/div[3]/div[1]/div[8]/pre")

		if description_pred != description_next:
			break

