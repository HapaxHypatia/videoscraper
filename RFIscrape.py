import time
from selenium.common import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.by import By
# TODO not locating video elements

def RFIscrape(driver, url):
	denyCookies = '/html/body/div[1]/div/div/div/div/div/div[3]/button[2]'
	time.sleep(3)
	try:
		driver.find_element(by=By.XPATH, value=denyCookies).click();
	except (NoSuchElementException, ElementNotInteractableException):
		pass
	contents = []

	while True:
		videos = driver.find_elements(by=By.CLASS_NAME, value='m-podcast-item')
		print(len(videos))
		for video in videos[1:]:
			# get data
			title = video.find_element(by=By.XPATH, value='//a[1]').get_attribute('title')
			print(title)
			link = video.find_element(by=By.XPATH, value='//a[1]').get_attribute('href')
			print(link)
			image = video.find_element(by=By.XPATH, value='//a/figure/picture/img').get_attribute('src')
			# date = video.find_element(by=By.TAG_NAME, value='time').text
			contents.append(
				{
					"title": title,
					"channel": "RFI français facile",
					"image": image,
					"link": link,
					"description": "",
					"date": ""
				}

			)
		try:
			nextPage = driver.find_element(by=By.XPATH, value='//*/a[@title="Next page"]')
			driver.execute_script('arguments[0].click()', nextPage)
			time.sleep(4)
		except (NoSuchElementException, ElementNotInteractableException):
			break
	return contents
