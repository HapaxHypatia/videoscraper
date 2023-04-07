from selenium.common import TimeoutException
from selenium.webdriver.common.by import By

def CBFscrape(driver, url):

	def get_videos(url):
		driver.get(url)
		videos = driver.find_elements(By.TAG_NAME, value='article')
		videodata = []
		for video in videos:
			# get data
			title = video.find_element(by=By.XPATH, value='.//h3/a').text
			link = video.find_element(by=By.XPATH, value='.//h3/a').get_attribute('href')
			image = video.find_element(by=By.XPATH, value='.//img').get_attribute('src')
			description = video.find_element(by=By.XPATH, value='.//*[@class="elementor-post__excerpt"]/p').text
			if "cbf-season-1" in url:
				level = "Beginner"
			if "cbf-season-2" in url or "cbf-season-3" in url:
				level = 'Intermediate'
			if "cbf-season-4" in url:
				level = 'Advanced'
			else:
				level = ""

			videodata.append(
				{
					"title": title,
					"channel": "Coffee Break French",
					"image": image,
					"link": link,
					"description": description,
					"date": '',
					"level": level
				}

			)
		return videodata

	contents = get_videos(url)
	for i in range(2, 4):
		try:
			nextPage = (url + 'page/' + str(i))
			contents += get_videos(nextPage)
		except TimeoutException:
			continue

	print("Total Videos = ", len(contents))
	return contents
