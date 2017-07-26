from selenium import webdriver
import bs4, sys, os, time


def login(browser, login_url):
	browser.get(login_url)
	browser.maximize_window()
	browser.implicitly_wait(1)
	userNameElem = browser.find_element_by_id('username')
	userNameElem.clear()
	userNameElem.send_keys('你的用户名')
	passwordElem = browser.find_element_by_id('password')
	userNameElem.clear()
	passwordElem.send_keys('你的密码')
	passwordElem.submit()
	time.sleep(1)	
	# without waiting, the website doesn't have time to log in et register the information.


#USING PHANTOMJS for headless browsing (without opening a mozilla window)

browser        = webdriver.PhantomJS()


# LOG in lang8
login_url  = "https://lang-8.com/login"
yamasvPage = "http://lang-8.com/177146/journals?page=" # your interested user profile page
login(browser, login_url)

first_page  = 1
last_page   = 30

print ("Start downloading....\n")

for page_index in range(first_page, last_page+1):
	print ("Now downloading page: " + str(page_index))
	browser.get(yamasvPage + str(page_index))
	entries_page = browser.page_source
	soup         = bs4.BeautifulSoup(entries_page,"lxml")
	entries_elem = soup.select('.journal_title a')
	for entry in reversed(entries_elem):
		entry_link  = entry.get("href")
		browser.get(entry_link)
		entry_page  = browser.page_source
		soup        = bs4.BeautifulSoup(entry_page,"lxml")

		entry_text  = soup.select('#body_show_ori')
		entry_text  = str(entry_text[0]).replace("<div id=\"body_show_ori\">", "") \
                                  .replace("</div>","").replace("<br/>","\n")
		f           = open("mogu.txt","a", encoding="utf-8")
		f.write(entry_text)
		f.close()
'''		
		entry_text_jp  = soup.select('#body_show_mo')
		entry_text_jp  = str(entry_text_jp[0]).replace("<div id=\"body_show_mo\">", "") \
                                  .replace("</div>","").replace("<br/>","\n") 
		f              = open("mogu.txt","a", encoding="utf-8")
		f.write(entry_text_jp)
		f.close()
'''

	
               
		
print ("\n----------------------------------\n")
print("DONE downloaded all entries.\n")
