import time
from selenium.common import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.by import By


def RFIscrape(driver):
	denyCookies = '/html/body/div[1]/div/div/div/div/div/div[3]/button[2]'
	time.sleep(3)
	try:
		driver.find_element(by=By.XPATH, value=denyCookies).click();
	except (NoSuchElementException, ElementNotInteractableException):
		pass
	contents = []
	while True:
		videos = driver.find_elements(By.CSS_SELECTOR, value='.m-item-list-article')
		for video in videos[1:]:
			# get data
			title = video.find_element(by=By.XPATH, value='.//a/div/p').text
			link = video.find_element(by=By.XPATH, value='.//a').get_attribute('href')
			image = video.find_element(by=By.XPATH, value='.//a/div[1]/figure/picture/img').get_attribute('src')
			# date = video.find_element(by=By.TAG_NAME, value='time').text
			contents.append(
				{
					"title": title,
					"channel": "RFI français facile",
					"image": image,
					"link": link,
					# "date": date
				}

			)
		try:
			nextPage = driver.find_element(by=By.XPATH, value='//*/a[@title="Next page"]')
			driver.execute_script('arguments[0].click()', nextPage)
			print("Clicked next page")
			time.sleep(4)
		except (NoSuchElementException, ElementNotInteractableException):
			break
	print("Total Videos = ", len(contents))
	return contents