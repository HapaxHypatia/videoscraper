from selenium.webdriver.common.by import By

def FLEscrape(driver):
	list = driver.find_element(by=By.XPATH, value="/html/body/div[4]/div/div[1]/div[1]/div[1]/div/div/table[2]")

