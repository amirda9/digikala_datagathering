from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd


driver = webdriver.Chrome('/home/amir/Downloads/chromedriver_linux64/chromedriver')

for i in range(1,10): 
    # print(f"amir{i}")   
    driver.get(f"https://www.digikala.com/search/category-mobile-phone/?pageno={i}&sortby=4")
    labels=driver.find_elements_by_css_selector(".js-product-url")
    with open('pages.txt', 'a') as f:
        for label in labels:
            f.write(label.get_attribute('href')+'\n')

with open('pages.txt') as f:
    lines = f.readlines()

# labels =[]
for line in lines:
    driver.get(line)
    labels=driver.find_elements_by_css_selector(".c-comments__content")
    with open('readme.txt', 'a') as f:
        for label in labels:
            f.write(label.text+'\n')
    
driver.close()