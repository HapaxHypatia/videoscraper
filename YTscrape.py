from selenium.webdriver.common.by import By
import time
import re

def YTscrape(driver, url):
	channel = url.split('@')[1].replace("/videos", "")
	print(channel)
	# scroll page
	for i in range(30):
		document_height = driver.execute_script("return document.documentElement.scrollHeight")
		driver.execute_script(f"window.scrollTo(0, {document_height	+ 2000});")
		time.sleep(1)

	# get list of videos
	videos = driver.find_elements(by=By.ID, value='dismissible')
	print("Total Videos = ", len(videos))
	contents = []
	for video in videos:
		# get data
		title = video.find_element(by=By.XPATH, value='.//*[@id="video-title"]').text
		image = video.find_element(by=By.XPATH, value='.//*[@id="thumbnail"]/yt-image/img').get_attribute('src')
		link = video.find_element(by=By.XPATH, value='.//*[@id="video-title-link"]').get_attribute('href')
		date = video.find_element(by=By.XPATH, value='.//*[@id="metadata-line"]/span[2]').text
		if 'years' in date:
			years = int(re.findall("\d+", date)[0]) # skip videos older than 5 years
			if years > 5:
				continue

		contents.append(
			{
				"title": title,
				"image": image,
				"channel": channel,
				"link": link,
				"date": date
			}

		)

	return contents

