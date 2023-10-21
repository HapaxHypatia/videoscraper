from selenium.webdriver.common.by import By

def iliniScrape(driver, url):
	contents = []
	videos = driver.find_elements(by=By.CSS_SELECTOR, value=".bottom-margin-on-medium-up")
	print("No of videos = {}".format(len(videos)))
	if "beginner" in url:
		level = "beginner"
	if "intermediate" in url:
		level = 'intermediate'
	if "advanced" in url:
		level = 'advanced'
	else:
		level = ""
	for video in videos:
		link = video.find_element(by=By.XPATH, value=".//a").get_attribute('href')
		title = video.find_element(by=By.CSS_SELECTOR, value=".title").get_attribute('text')
		image = video.find_element(by=By.TAG_NAME, value="img").get_attribute('src')
		description = ''

		contents.append(
			{
				"title": title,
				"channel": "Partajon",
				"image": image,
				"link": link,
				"description": description,
				"date": "",
				"level": level
			})
	return contents
