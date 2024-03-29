from selenium.common import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.by import By
import time

def unjourScrape(driver, url):
	time.sleep(3)
	try:
		driver.find_element(by=By.CLASS_NAME, value="didomi-continue-without-agreeing").click();
		print("Denied cookies")
		time.sleep(3)
	except (NoSuchElementException, ElementNotInteractableException):
		pass

	videos = driver.find_elements(By.TAG_NAME, value='article')
	contents = []
	time.sleep(3)
	for video in videos:
		# get data
		title = video.find_element(by=By.XPATH, value='.//div/a[1]').get_attribute('title')
		link = video.find_element(by=By.XPATH, value='.//div/a[1]').get_attribute('href')
		image = video.find_element(by=By.XPATH, value='//div/div[1]/a/img').get_attribute('src')
		contents.append(
			{
				"title": title,
				"channel": "Un jour une actu",
				"image": image,
				"link": link,
				"description": "",
				"date": ""
			}

		)
	return contents
