from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.by import By

# Lawless has a security pop-up after awhile. Can't do too many of their sites in a row

def LFscrape(driver, url):
	videos = driver.find_elements(By.TAG_NAME, value='article')
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
				"channel": "Lawless French",
				"image": image,
				"link": link,
				"description": description,
				"date": "",
				"level": level
			}

		)
	return contents