import requests
from bs4 import BeautifulSoup
from googlesearch import search
import schedule
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
driver = webdriver.Chrome('./chromedriver')
#accessing the wbpage
driver.get("https://octopart.com/")
# create action chain object
action = ActionChains(driver)

search_box = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div[2]/input")
search_box.send_keys("CMX100D6")
search_box.send_keys(Keys.RETURN)
driver.implicitly_wait(10)
proceed = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/div[2]/div[1]/div[1]/div[1]/div/a/div[2]/span/mark")
proceed.click()

action.context_click().send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.RETURN).send_keys(Keys.RETURN).perform()













