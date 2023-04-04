from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import json
from YTscrape import YTscrape
from lawlessScrape import LFscrape
from CBFscrape import CBFscrape
from FLEscrape import FLEscrape
from TEFscrape import TEFscrape
from unjourScrape import unjourScrape

with open("urls.txt", 'r') as f:
	urls = [x.strip() for x in f.readlines()]
driver = webdriver.Chrome(ChromeDriverManager().install())
data = []
# TODO look into decorator functions rather than repeating code each time.
for url in urls:
	driver.get(url)
	print('Looking for videos at ', url)
	if "youtube" in url:
		YTdata = YTscrape(driver, url)
		print(len(YTdata), " videos found at ", url)
		print("Data collection complete.")
		data = data+YTdata
	if "lawlessfrench" in url:
		LFdata = LFscrape(driver)
		print(len(LFdata), " videos found at ", url)
		data = data+LFdata
	if "coffeebreaklanguages" in url:
		CBFdata = CBFscrape(driver)
		print(len(CBFdata), " videos found at ", url)
		data = data+CBFdata
	if "flevideo" in url:
		FLEdata = FLEscrape(driver, url)
		print(len(FLEdata), " videos found at ", url)
		data = data+FLEdata
	if "toutenfrancais" in url:
		TEFdata = TEFscrape(driver)
		print(len(TEFdata), " videos found at ", url)
		data = data+TEFdata
	if "1jour" in url:
		unjourdata = unjourScrape(driver)
		print(len(unjourdata), " videos found at ", url)
		data = data+unjourdata



print("Total videos found = ", len(data))
with open('C:\projects\listening-search\src\data.json', 'w') as f:
	json.dump(data, f)
print("Video data saved.")
driver.close()


