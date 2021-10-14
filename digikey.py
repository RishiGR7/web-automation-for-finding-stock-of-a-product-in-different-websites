from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
driver = webdriver.Chrome('./chromedriver')
driver.get("https://www.digikey.in/")
search_box = driver.find_element_by_xpath('/html/body/header/div[1]/div[1]/div/div[2]/div[2]/input')
search_box.send_keys("CMX100D6")
search_box.send_keys(Keys.RETURN)
option = driver.find_element_by_xpath('/html/body/div[2]/main/div/div/div/div[4]/div[2]/div/div/div/div/div/div[2]/div/a/span')
option.click()
stock = driver.find_element_by_xpath('/html/body/div[2]/main/div/div[2]/div/div[3]/div/div[2]/div')
stock.click()
email = driver.find_element_by_xpath('/html/body/div[9]/div[3]/div/div[2]/div/span/span/div[2]/div[2]/input')
email.send_keys('ravindragavirneni83@gmail')
notify = driver.find_element_by_xpath('/html/body/div[9]/div[3]/div/div[3]/div/button/span')
notify.click()
driver.close()
