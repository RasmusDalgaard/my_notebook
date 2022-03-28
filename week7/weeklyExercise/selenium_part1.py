import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.headless = True
browser = webdriver.Firefox(options=options)

browser.get('http://www.dba.dk')
browser.implicitly_wait(2)

searchField = browser.find_element_by_id('searchField')
searchField.send_keys('PS5')
searchField.submit()

browser.implicitly_wait(2)


createdCollapseBar = browser.find_element_by_css_selector('#srpNavigators > div:nth-child(4)')
createdCollapseBar.click()

#Kan ikke finde ud af at klikke en radiobox på DBA så det virker ikke
radiobox48hours = browser.find_element_by_css_selector('#srpNavigators > div:nth-child(4) > div > ul > li:nth-child(2)')
radiobox48hours.click()



