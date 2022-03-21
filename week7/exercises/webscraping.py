import webbrowser
import requests
import bs4
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def get_all_links():

    r = requests.get('https://www.cphbusiness.dk')
    r.raise_for_status()
    soup = bs4.BeautifulSoup(r.text, 'html.parser')

    for link in soup.find_all('a'):
        links = []
        if 'https' not in str(link.get('href')):
            continue
        print(link.get('href'))
        links.append(link)
    return links

#doesn't work
def get_links_of_links():
    options = Options()
    options.headless = True
    browser = webdriver.Chrome(options=options)
    browser.get('https://www.cphbusiness.dk')
    browser.implicitly_wait(3)
    for link in get_all_links():
        link_button = browser.find_element_by_link_text(link)
        link_button.click()
        links = browser.find_elements_by_css_selector('a.href')
        for link_ in links:
            print(link_)


#get_links_of_links()