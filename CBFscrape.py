from selenium.webdriver.common.by import By

def CBFscrape(driver):
	videos = driver.find_elements(By.TAG_NAME, value='article')
	print("Total Videos = ", len(videos))
	contents = []
	for video in videos:
		# get data
		title = video.find_element(by=By.XPATH, value='.//h3/a').text
		link = video.find_element(by=By.XPATH, value='.//h3/a').get_attribute('href')
		image = video.find_element(by=By.XPATH, value='.//img').get_attribute('src')
		description = video.find_element(by=By.XPATH, value='.//*[@class="elementor-post__excerpt"]/p').text
		contents.append(
			{
				"title": title,
				"channel": "Coffee Break French",
				"image": image,
				"link": link,
				"description": description
			}

		)
	return contents
