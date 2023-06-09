from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
import time

def TEFscrape(driver, url):
	contents = []
	num_videos = 0
	while True:
		time.sleep(5)
		videos = driver.find_elements(by=By.XPATH, value='//*[@id="hits"]/div/div/ol/li')
		if len(videos) > num_videos:
			num_videos = len(videos)
		else:
			break
		for video in videos:
			image = video.find_element(by=By.CLASS_NAME, value='search-thumbnail').get_attribute('src')
			link = video.find_element(by=By.XPATH, value='.//div/div[1]/div[1]/a[2]').get_attribute('href')
			title = link.split('/')[3].replace('-', ' ')
			description = video.find_element(by=By.XPATH, value='.//li/div/div[1]/div[2]/p[2]').text
			tagElements = video.find_elements(by=By.XPATH, value='//*[@id="hits"]/div/div/ol/li[1]/li/div/div[1]/div[2]/p[3]/span[1]')
			tags = []
			for elem in tagElements:
				tags.append(elem.text)
			if not any(d['title'] == title for d in contents):
				contents.append(
					{
						"title": title,
						"channel": "Tout en Français",
						"image": image,
						"link": link,
						"description": description,
						# "tags": tags
						"date": ""
					}
					)
		try:
			loadmore = driver.find_element(by=By.XPATH, value='//*[@id="hits"]/div/div/button')
			driver.execute_script('arguments[0].click()', loadmore)
		except (NoSuchElementException, ElementNotInteractableException):
			print('loadmore button not found')
			break
	return contents
