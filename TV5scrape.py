import time
from selenium.common import NoSuchElementException, StaleElementReferenceException, ElementNotInteractableException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def TV5scrape(driver):
	denyCookies = '//*[@id="didomi-notice-disagree-button"]'
	time.sleep(3)
	try:
		driver.find_element(by=By.XPATH, value=denyCookies).click();
		print("denied cookies")
		time.sleep(3)
	except (NoSuchElementException, ElementNotInteractableException):
		pass

	count = 0
	while True:
		try:
			loadmore = driver.find_element(by=By.XPATH, value='//a[@title="Load more items"]')
			driver.execute_script('arguments[0].click()', loadmore)
			count += 1
			print("loadmore clicked: ", count)
			time.sleep(1)
		except (NoSuchElementException, ElementNotInteractableException, StaleElementReferenceException):
			break

	contents = []
	videos = driver.find_elements(By.CLASS_NAME, value='views-row')
	for video in videos[1:]:
		# get data
		title = video.find_element(by=By.XPATH, value='a/div/div[2]/div[1]/h2').text
		link = video.find_element(by=By.XPATH, value='.//a').get_attribute('href')
		picture = video.find_element(by=By.TAG_NAME, value='picture')
		image = picture.find_element(by=By.TAG_NAME, value='img').get_attribute('src')
		description = video.find_element(by=By.CSS_SELECTOR, value='.special-search-excerpt').text
		level = video.find_element(by=By.XPATH, value='.//a/div/div[2]/div[2]/div[1]/span').text

		contents.append(
			{
				"title": title,
				"channel": "TV5",
				"image": image,
				"link": link,
				"description": description,
				# "level": level
				"date": ""
			}

		)

	print("Total Videos = ", len(contents))
	return contents
