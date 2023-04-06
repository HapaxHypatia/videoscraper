import time
from selenium.common import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.by import By


def TV5scrape(driver):
	denyCookies = '//*[@id="didomi-notice-disagree-button"]'
	time.sleep(3)
	try:
		driver.find_element(by=By.XPATH, value=denyCookies).click();
	except (NoSuchElementException, ElementNotInteractableException):
		pass
	contents = []
	while True:
		videos = driver.find_elements(By.CLASS_NAME, value='views-row')
		for video in videos[1:]:
			# get data
			title = video.find_element(by=By.XPATH, value='a/div/div[2]/div[1]/h2').text
			link = video.find_element(by=By.XPATH, value='.//a').get_attribute('href')
			image = video.find_element(by=By.XPATH, value='.//a/div/div[1]/div/div[1]/div/picture/img').get_attribute('src')
			description = video.find_element(by=By.XPATH, value='.//a/div/div[2]/div[1]/div[2]')
			level = video.find_element(by=By.XPATH, value='.//a/div/div[2]/div[2]/div[1]/span')

			contents.append(
				{
					"title": title,
					"channel": "TV5",
					"image": image,
					"link": link,
					"description": description,
					"level": level
				}

			)
		try:
			loadmore = driver.find_element(by=By.XPATH, value='/html/body/div[2]/div[4]/div/section/div[2]/div/div/ul/li/a')
			driver.execute_script('arguments[0].click()', loadmore)
		except (NoSuchElementException, ElementNotInteractableException):
			break
	print("Total Videos = ", len(contents))
	return contents
