from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

def PFFscrape(driver, url):
	stem = '/html/body/div[1]/div/main/div/section/div/div/div['
	videos = []
	for i in range(1, 5):
		for j in range(1, 5):
			for k in range(1, 5):
				try:
					videos = videos+(driver.find_elements(By.XPATH,
					value = stem+str(i)+']/div/div['+str(j)+']/div/div['+str(k)+']/p/a'))
				except NoSuchElementException:
					continue

	contents = []
	for video in videos:
		# get data
		title = video.text
		link = video.get_attribute('href')
		contents.append(
			{
				"title": title,
				"channel": "Podcast Français Facile",
				"image": "",
				"link": link,
				"description": "",
				"date": ""
			}
		)
	return contents


# TODO Code this url separately
# https://www.podcastfrancaisfacile.com/dialogue-francais-avance-apprendre-francais
