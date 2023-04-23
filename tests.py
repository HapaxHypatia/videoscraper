from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import json
import time

from PFFscrape import PFFscrape
from RFIscrape import RFIscrape
from TV5scrape import TV5scrape
from YTscrape import YTscrape
from lawlessScrape import LFscrape
from CBFscrape import CBFscrape
from FLEscrape import FLEscrape
from TEFscrape import TEFscrape
from unjourScrape import unjourScrape

start = time.time()
urls = [
'https://coffeebreaklanguages.com/tag/cbf-er-season-1/',
'https://www.youtube.com/@Commeunefrancaise/videos',
'https://apprendre.tv5monde.com/fr/search/site?f%5B0%5D=im_field_competence%3A61&f%5B1%5D=im_field_competence%3A222&f%5B2%5D=im_field_niveau%3A371&f%5B3%5D=type_de_contenu%3Aserie_exercices',
'https://francaisfacile.rfi.fr/en/podcasts/journal-en-fran%C3%A7ais-facile/',
'https://www.podcastfrancaisfacile.com/apprendre-le-francais/videos-en-francais',
'https://toutenfrancais.tv/category/lactu-tout-en-francais/',
'https://www.1jour1actu.com/videos',
'https://www.lawlessfrench.com/faq/lessons-by-level/a1-listening/',
'https://www.flevideo.com/fle_video_quiz_low_intermediate_start.php'
]

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.set_page_load_timeout(60)
data = []
for url in urls:
	driver.get(url)
	if "youtube" in url:
		YTdata = YTscrape(driver, url)
		data = data+YTdata
	if "lawlessfrench" in url:
		LFdata = LFscrape(driver, url)
		print(len(LFdata), " videos found at ", url)
		data = data+LFdata
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

with open("test_data.json", 'w') as f:
	json.dump(data)
print('Completed test in ', str(round(time.time()-start)/60))