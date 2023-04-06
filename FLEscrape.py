from selenium.webdriver.common.by import By
import time
def FLEscrape(driver, url):
	pages =driver.find_element(by=By.XPATH, value="/html/body/div[4]/div/div[1]/div[1]/div[1]/div/div/b[2]").text
	print("Number of pages = ", pages)
	query = '?pagenum='
	contents = []
	for i in range(1, int(pages)+1):
		driver.get(url+query+str(i))
		time.sleep(2)
		videolist = driver.find_element(by=By.XPATH, value=".//table[2]")
		videos = videolist.find_elements(by=By.TAG_NAME, value='p')

		for video in videos:
			# get data
			title = video.find_element(by=By.XPATH, value='.//a[2]').text
			image = video.find_element(by=By.XPATH, value='.//img').get_attribute('src')
			link = video.find_element(by=By.XPATH, value='.//a[2]').get_attribute('href')

			contents.append(
				{
					"title": title,
					"channel": "FLE Video",
					"image": image,
					"link": link,
					"description": "",
					"date": ""
				}

			)
	return contents
