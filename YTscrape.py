from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import json

urls = [
'https://www.youtube.com/@EasyFrench/videos',
'https://www.youtube.com/@Commeunefrancaise/videos',
'https://www.youtube.com/@FluentUFrench/videos',
'https://www.youtube.com/@innerFrench/videos',
'https://www.youtube.com/@FrancaisavecPierre/videos',
'https://www.youtube.com/@digiSchool-college/videos'
]

driver = webdriver.Chrome(ChromeDriverManager().install())
contents = []
for url in urls:
	driver.get(url)

	# scroll page
	for i in range(25):
		document_height = driver.execute_script("return document.documentElement.scrollHeight")
		driver.execute_script(f"window.scrollTo(0, {document_height	+ 2000});")
		time.sleep(1)

	# harvest videos
	videos = driver.find_elements(by=By.ID, value='dismissible')
	print("Videos = ", len(videos))

	for video in videos:
		# get data
		title = video.find_element(by=By.XPATH, value='.//*[@id="video-title"]').text
		image = video.find_element(by=By.XPATH, value='.//*[@id="thumbnail"]/yt-image/img').get_attribute('src')
		link = video.find_element(by=By.XPATH, value='.//*[@id="video-title-link"]').get_attribute('href')
		date = video.find_element(by=By.XPATH, value='.//*[@id="metadata-line"]/span[2]').text

		contents.append(
			{
				"title": title,
				"image": image,
				"link": link,
				"date": date
			}

		)
	print(url, " complete.")

with open('C:\projects\listening-search\src\ytdata.json', 'w') as f:
	json.dump(contents,f)
driver.close()