from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.by import By


def LFscrape(driver):
	# try:
	#     driver.find_element(By.CLASS_NAME, 'cp-popup-content').click()
	#     print('pop-up closed')
	# except (NoSuchElementException, ElementNotInteractableException):
	#     pass
	videos = driver.find_elements(By.TAG_NAME, value='article')
	print("Total Videos = ", len(videos))
	contents = []
	for video in videos:
		# get data
		title = video.find_element(by=By.XPATH, value='.//header/h2').text
		try:
			table =video.find_element(by=By.XPATH, value='.//table')
		except NoSuchElementException:
			print('Skipping misc links - not a video.')
			continue
		image = video.find_element(by=By.XPATH, value='.//img').get_attribute('src')
		link = video.find_element(by=By.XPATH, value='.//header/h2').get_attribute('href')
		description = video.find_element(by=By.CLASS_NAME, value='entry-summary').text

		contents.append(
			{
				"title": title,
				"channel": "Lawless French",
				"image": image,
				"link": link,
				"description": description
			}

		)
	return contents