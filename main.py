import random

from git import Repo
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from PFFscrape import PFFscrape
from RFIscrape import RFIscrape
from TV5scrape import TV5scrape
from YTscrape import YTscrape
from lawlessScrape import LFscrape
from CBFscrape import CBFscrape
from FLEscrape import FLEscrape
from TEFscrape import TEFscrape
from partajon import PJscrape
from unjourScrape import unjourScrape
from iliniScrape import iliniScrape
import time
import json
from datetime import datetime as dt

start = time.time()
logfile = open("logs.txt", 'a')
now = dt.now().strftime('%a %d/%m/%Y %H:%M:%S')
logfile.write("\n\n\nStarting run at {0} \n".format(now))

with open('C:\projects\listening-search\src\data.json', 'r') as f:
	prev = len(json.load(f))
	logfile.write("Previous number of videos = {0}\n".format(prev))

with open("urls.txt", 'r') as f:
	urls = [x.strip() for x in f.readlines()]

functions = {
	"youtube": YTscrape,
	"lawlessfrench": LFscrape,
	"coffeebreaklanguages": CBFscrape,
	"flevideo": FLEscrape,
	"toutenfrancais": TEFscrape,
	"1jour": unjourScrape,
	"podcastfrancaisfacile":PFFscrape,
	"rfi": RFIscrape,
	"tv5": TV5scrape,
	"partajon": PJscrape,
	"ilini": iliniScrape
}

try:
	service = Service()
	options = webdriver.ChromeOptions()
	options.add_argument('start-maximized')
	# options.add_argument("--headless") #doesn't open window
	# options.add_argument(f'--proxy-server={proxy}')
	driver = webdriver.Chrome(service=service, options=options)
	driver.set_page_load_timeout(60)

	data = []
except Exception as e:
	error_message = str(e)
	logfile.write(dt.now().strftime('%a %d/%m/%Y %H:%M:%S\n'))
	logfile.write('Error in loading webdriver')
	logfile.write(error_message)

for url in urls:
	try:
		driver.get(url)
		print('Looking for videos at ', url)
		for channel in functions.keys():
			if channel in url:
				tempdata = functions[channel](driver, url)
				logfile.write("{0} videos found at {1}\n".format(len(tempdata), url))
				data += tempdata
				logfile.write("Data collection complete.\n")
	except Exception as e:
		error_message = str(e)
		logfile.write(dt.now().strftime('%a %d/%m/%Y %H:%M:%S\n'))
		logfile.write('Error during data collection at {}\n'.format(url))
		logfile.write(error_message)
		continue

unique = []
for i in range(len(data)):
	if data[i] not in data[i + 1:]:
		unique.append(data[i])
if len(data) > prev-100:
	f = open('C:\projects\listening-search\src\data.json', 'w')
	json.dump(unique, f)
	f.close()
	repo_path = "C:/projects/listening-search"
	repo = Repo(repo_path)

	repo.git.add("C:/projects/listening-search/src/data.json")
	logfile.write("added data file\n")
	repo.index.commit('auto committing data changes')
	logfile.write("committed file\n")
	repo.remotes.origin.push(repo.head)
	logfile.write("pushed file to master\n")

	repo.heads.production.checkout()
	repo.git.add("C:/projects/listening-search/src/data.json")
	logfile.write("added data file\n")
	repo.index.commit('auto committing data changes')
	logfile.write("committed file\n")
	repo.remotes.origin.push(repo.head)
	logfile.write("pushed file to production\n")


logfile.write("Total videos found = {0}\n\n".format(len(unique)))
driver.close()
logfile.write('Completed run in {0} seconds\n\n\n\n\n\n'.format(str((time.time()-start)//60)))
