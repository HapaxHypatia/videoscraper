from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import json
from YTscrape import YTscrape
from lawlessScrape import LFscrape
from CBFscrape import CBFscrape


with open("urls.txt", 'r') as f:
	urls = [x.strip() for x in f.readlines()]
driver = webdriver.Chrome(ChromeDriverManager().install())
data = []
# TODO look into decorator functions rather than repeating code each time.
for url in urls:
	driver.get(url)
	print('Looking for videos at ', url)
	if "youtube" in url:
		YTdata = YTscrape(driver)
		print(len(YTdata), " videos found at ", url)
		print("Data collection complete.")
		data = data+YTdata
	if "lawlessfrench" in url:
		LFdata = LFscrape(driver)
		print(len(YTdata), " videos found at ", url)
		data = data+LFdata
	if "coffeebreaklanguages" in url:
		CBFdata = CBFscrape(driver)
		print(len(YTdata), " videos found at ", url)
		data = data+CBFdata

print("Total videos found = ", len(data))
with open('C:\projects\listening-search\src\data.json', 'w') as f:
	json.dump(data, f)
driver.close()


