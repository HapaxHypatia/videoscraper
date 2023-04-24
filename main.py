from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import json
from PFFscrape import PFFscrape
from RFIscrape import RFIscrape
from TV5scrape import TV5scrape
from YTscrape import YTscrape
from lawlessScrape import LFscrape
from CBFscrape import CBFscrape
from FLEscrape import FLEscrape
from TEFscrape import TEFscrape
from unjourScrape import unjourScrape
import time
import json

start = time.time()
with open('C:\projects\listening-search\src\data.json', 'r') as f:
	prev = len(json.load(f))
with open("urls.txt", 'r') as f:
	urls = [x.strip() for x in f.readlines()]

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.set_page_load_timeout(60)
data = []


def save(data):
	unique = []
	for i in range(len(data)):
		if data[i] not in data[i + 1:]:
			unique.append(data[i])
	f = open('C:\projects\listening-search\src\data.json', 'w')
	json.dump(unique, f)
	f.close()


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
		LFdata = LFscrape(driver, url)
		print(len(LFdata), " videos found at ", url)
		data = data+LFdata
		save(data)
	if "coffeebreaklanguages" in url:
		CBFdata = CBFscrape(driver, url)
		print(len(CBFdata), " videos found at ", url)
		data = data+CBFdata
	if "flevideo" in url:
		FLEdata = FLEscrape(driver, url)
		print(len(FLEdata), " videos found at ", url)
		data = data+FLEdata
	if "toutenfrancais" in url:
		TEFdata = TEFscrape(driver, url)
		print(len(TEFdata), " videos found at ", url)
		data = data+TEFdata
	if "1jour" in url:
		unjourdata = unjourScrape(driver, url)
		print(len(unjourdata), " videos found at ", url)
		data = data+unjourdata
	if "podcastfrancaisfacile" in url:
		PFFdata = PFFscrape(driver, url)
		print(len(PFFdata), " videos found at ", url)
		data = data + PFFdata
	if "rfi" in url:
		RFIdata = RFIscrape(driver, url)
		print(len(RFIdata), " videos found at ", url)
		data = data + RFIdata
	if "tv5" in url:
		TV5data = TV5scrape(driver, url)
		print(len(TV5data), " videos found at ", url)
		data = data + TV5data

if len(data) > prev:
	save(data)
print("Total videos found = ", len(data))
driver.close()
print('Completed test in ', str(round(time.time()-start)/60),'seconds')
