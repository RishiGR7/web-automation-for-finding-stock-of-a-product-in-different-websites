from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome('./chromedriver')
#accessing the wbpage
driver.get("https://google.com")
driver.maximize_window()
search = driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
search.send_keys("uwb3 rf space")
search.send_keys(Keys.RETURN)
amazon = driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div/div[1]/a/h3')
#amazon = driver.find_element_by_xpath('/html/body/div[7]/div/div[9]/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/a/h3')
amazon.click()
try:
    driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[5]/div[4]/div[1]/div[3]/div/div/div/form/div/div/div[1]/span')
    print('stock Currently unavailable.')
except NoSuchElementException:
    print('stock exists')

driver.close()

