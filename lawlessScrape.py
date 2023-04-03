from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import json

urls = [
'https://www.lawlessfrench.com/faq/lessons-by-level/a1-listening/',
'https://www.lawlessfrench.com/faq/lessons-by-level/a2-listening/',
'https://www.lawlessfrench.com/faq/lessons-by-level/b1-listening/',
'https://www.lawlessfrench.com/faq/lessons-by-level/b2-listening/',
'https://www.lawlessfrench.com/faq/lessons-by-level/c1-listening/'
]

driver = webdriver.Chrome(ChromeDriverManager().install())
contents = []
for url in urls:
	driver.get(url)
	videos = driver.find_elements(By.TAG_NAME, value='article')
	print("Videos = ", len(videos))

	for video in videos:
		# get data
		title = video.find_element(by=By.XPATH, value='.//').text
		image = video.find_element(by=By.XPATH, value='.//').get_attribute('src')
		link = video.find_element(by=By.XPATH, value='.//').get_attribute('href')
		date = video.find_element(by=By.XPATH, value='.//').text



