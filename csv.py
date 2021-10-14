

# import the webdriver
from selenium import webdriver
# import the Keys class
from selenium.webdriver.common import keys
driver = webdriver.Chrome ("./chromedriver")
# get method to launch the URL
driver.get("https://octopart.com/ms25042-14da-glenair-932863")
# to identify the table rows
l = driver.find_elements_by_xpath ("/html/body/div[1]/div[3]/div/div[2]/div[2]/table[1]")
# to get the row count len method
print (len(l))
# to close the browser
driver.quit ()