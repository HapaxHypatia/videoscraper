from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import json
from PFFscrape import PFFscrape
from RFIscrape import RFIscrape
from YTscrape import YTscrape
from lawlessScrape import LFscrape
from CBFscrape import CBFscrape
from FLEscrape import FLEscrape
from TEFscrape import TEFscrape
from unjourScrape import unjourScrape

with open("urls.txt", 'r') as f:
	urls = [x.strip() for x in f.readlines()]

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.set_page_load_timeout(60)
data = []
f = open('C:\projects\listening-search\src\data.json', 'w')

# TODO look into decorator functions rather than repeating code each time.
for url in urls:
	driver.get(url)
	print('Looking for videos at ', url)
	if "youtube" in url:
		YTdata = YTscrape(driver, url)
		print(len(YTdata), " videos found at ", url)
		print("Data collection complete.")
		data = data+YTdata
		json.dump(data, f)
	if "lawlessfrench" in url:
		LFdata = LFscrape(driver)
		print(len(LFdata), " videos found at ", url)
		data = data+LFdata
		json.dump(data, f)
	if "coffeebreaklanguages" in url:
		CBFdata = CBFscrape(driver)
		print(len(CBFdata), " videos found at ", url)
		data = data+CBFdata
		json.dump(data, f)
	if "flevideo" in url:
		FLEdata = FLEscrape(driver, url)
		print(len(FLEdata), " videos found at ", url)
		data = data+FLEdata
		json.dump(data, f)
	if "toutenfrancais" in url:
		TEFdata = TEFscrape(driver)
		print(len(TEFdata), " videos found at ", url)
		data = data+TEFdata
		json.dump(data, f)
	if "1jour" in url:
		unjourdata = unjourScrape(driver)
		print(len(unjourdata), " videos found at ", url)
		data = data+unjourdata
		json.dump(data, f)
	if "podcastfrancaisfacile" in url:
		PFFdata = PFFscrape(driver)
		print(len(PFFdata), " videos found at ", url)
		data = data + PFFdata
		json.dump(data, f)
	if "rfi" in url:
		RFIdata = RFIscrape(driver)
		print(len(RFIdata), " videos found at ", url)
		data = data + RFIdata
		json.dump(data, f)

print("Total videos found = ", len(data))
driver.close()


