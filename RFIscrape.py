import time
from selenium.common import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def RFIscrape(driver):
	cookies = '/html/body/div[1]/div/div/div/div/div/div[3]/button[2]'
	WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, cookies))).click()
	videos = driver.find_elements(By.CSS_SELECTOR, value='.m-item-list-article')
	print("Videos initially found = ", len(videos))
	contents = []
	while True:
		for video in videos[1:]:
			# get data
			title = video.find_element(by=By.XPATH, value='//a').text
			link = video.find_element(by=By.XPATH, value='//a').get_attribute('href')
			image = video.find_element(by=By.XPATH, value='//a/div[1]/figure/picture/img').get_attribute('src')
			contents.append(
				{
					"title": title,
					"channel": "RFI français facile",
					"image": image,
					"link": link,
				}

			)
		try:
			nextPage = driver.find_element(by=By.XPATH,value='//a[@title="Next page"]')
			driver.execute_script('arguments[0].click()', nextPage)
		except (NoSuchElementException, ElementNotInteractableException):
			break
	print("Total Videos = ", len(contents))
	return contents
