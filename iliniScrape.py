from selenium.webdriver.common.by import By

def iliniScrape(driver, url):
	contents = []
	videos = driver.find_elements(by=By.CSS_SELECTOR, value=".image-wrap")
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
		link = ''
		title = ''
		image = ''
		desciption = ''

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
