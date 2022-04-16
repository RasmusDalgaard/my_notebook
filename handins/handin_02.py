import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import numpy as np

options = Options()
options.headless = True
browser = webdriver.Firefox(options=options)

#Opgave 1 - Er det fredag?
def erDetFredag():
    browser.get('https://www.erdetfredag.dk')
    browser.implicitly_wait(2)
    browser.maximize_window()

    answer = browser.find_element_by_id('answer').text
    print(answer)

#erDetFredag()

#Opgave 2 - top 5 opskrifter fra nemlig.com
#Doesn't work yet
def top5recipes():
    browser.get('https://www.nemlig.com')
    browser.implicitly_wait(2)
    browser.maximize_window()

    recipes = []
    #Decline cookies and navigate to most popular recipes
    browser.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div[1]/button[1]').click()
    browser.implicitly_wait(2)
    browser.find_element_by_xpath('/html/body/div[3]/div/header/div[3]/main-navigation/mega-menu[7]/div/div/a').click()
    browser.implicitly_wait(2)
    browser.find_element_by_xpath('/html/body/div[4]/main/div/leftmenu/div/div/ul[2]/li[2]/a').click()
    browser.implicitly_wait(2)
    #Gets the div which contains all recipe-divs
    allRecipes = browser.find_element_by_xpath('/html/body/div[4]/main/div/div/div/leftmenupage/section/div[1]/render-partial/div/recipelist-showall/div/div/div[1]')
    for divs in allRecipes:
        current_recipe_div = divs.find_element_by_xpath('//*[@id="page-content"]/div/leftmenupage/section/div[1]/render-partial/div/recipelist-showall/div/div/div[1]/recipelist-item[1]/div/div/div[2]')
        for elements in current_recipe_div:
            recipe_name = elements.find_element_by_xpath('//*[@id="page-content"]/div/leftmenupage/section/div[1]/render-partial/div/recipelist-showall/div/div/div[1]/recipelist-item[1]/div/div/div[2]/div[1]/a').text
            recipes.append(recipe_name)
    
    return recipes

#Opgave 3 - Totale pris på gær, minimælk, banan og tomatpasta fra nemlig.com
def total_price():
    browser.get('https://www.nemlig.com')
    browser.implicitly_wait(2)
    browser.maximize_window()

    items = ['gær', 'minimælk', 'banan', 'tomatpasta']
    integer_prices = []
    decimal_prices = []

    #Search for each item in the items list
    searchField = browser.find_element_by_xpath('//*[@id="site-header-search-field-main"]')
    searchField.click()
    for item in items:
        searchField.send_keys(item)
        searchField.submit()
        browser.implicitly_wait(2)
        
    #Get the integer of the price and the decimal of the price and add to seperate lists
        integer_price = float(browser.find_element_by_xpath('//*[@id="searchscrollable"]/div/searchresult/div[1]/div[3]/div[1]/div[1]/div[1]/productlist-item[1]/a/div/div[3]/pricecontainer/div/div[2]/span').text)
        integer_prices.append(integer_price)
    
        decimal_price = float(browser.find_element_by_xpath('//*[@id="searchscrollable"]/div/searchresult/div[1]/div[3]/div[1]/div[1]/div[1]/productlist-item[1]/a/div/div[3]/pricecontainer/div/div[2]/sup').text)/100
        decimal_prices.append(decimal_price)

        searchField.clear()
    
    #Add the two lists together and print total
    item_prices = np.add(integer_prices, decimal_prices)
    total = 0
    for i in range(0, len(item_prices)):    
       total = total + item_prices[i];    
    print(str(total) + ' kr.')
    return total 

#total_price()

#Opgave 4 - Lav et barchart over alle Womens Fiction bøger fra http://books.toscrape.com/catalogue/category/books/womens-fiction_9/index.html
#Sorter efter pris
def womens_fiction():
    browser.get('http://books.toscrape.com/catalogue/category/books/womens-fiction_9/index.html')
    browser.implicitly_wait(2)
    browser.maximize_window()

    titles = []
    prices = []

    booklist_container = browser.find_element_by_xpath('//*[@id="default"]/div/div/div/div/section/div[2]/ol')
    booklist = booklist_container.find_elements_by_tag_name('li')
    browser.implicitly_wait(5)
    for book in booklist:
        currentTitle = book.find_element_by_tag_name('img').get_attribute('alt')
        print(currentTitle)
        titles.append(currentTitle)
        browser.implicitly_wait(10)
        price = float(book.find_element_by_class_name('price_color').text.replace('£', ''))
        print(price)
        prices.append(price)

womens_fiction()

