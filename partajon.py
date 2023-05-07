import time

from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.by import By


def PJscrape(driver, url):
	contents = []
	while True:
		videos = driver.find_elements(by=By.CLASS_NAME, value='post-wrapper')
		print("Total Videos = ", len(videos))
		for video in videos:
			# get data
			title = video.find_element(by=By.CLASS_NAME, value='entry-title').text
			link = video.find_element(by=By.CLASS_NAME, value='entry-title').get_attribute('href')
			image = video.find_element(by=By.XPATH, value='.//div[1]/div/img').get_attribute('src')

			description = video.find_element(by=By.XPATH, value='.//div[2]/p[1]').text
			if "a1" in url:
				level = "A1"
			if "a2" in url :
				level = 'A2'
			if "b1" in url:
				level = 'B1'
			if "b2" in url:
				level = 'B2'
			if "c1" in url:
				level = 'C1'
			else:
				level = ""

			contents.append(
				{
					"title": title,
					"channel": "Partajon",
					"image": image,
					"link": link,
					"description": description,
					"date": "",
					"level": level
				}

			)
		try:
			nextPage = driver.find_element(by=By.CSS_SELECTOR, value='.next')
			driver.execute_script('arguments[0].click()', nextPage)
			print('next button clicked')
			time.sleep(4)
		except (NoSuchElementException, ElementNotInteractableException):
			break

	return contents