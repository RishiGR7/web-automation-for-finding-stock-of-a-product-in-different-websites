

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from skpy import Skype
ama = open('amazon.dox','r')
partnumber =ama.readlines()
driver = webdriver.Chrome('./chromedriver')
# accessing the wbpage
driver.get("https://google.com")
driver.maximize_window()
search = driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
search.send_keys(partnumber)
search.send_keys(Keys.RETURN)
amazon = driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div/div[1]/a/h3')

amazon.click()
try:
    driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[5]/div[4]/div[1]/div[3]/div/div/div/form/div/div/div[1]/span')

    print("currently unavaliable")



except NoSuchElementException:
    sk = Skype("username", "password")  # connect to Skype
    sk.user  # you
    sk.contacts  # your contacts
    sk.chats
    ch = sk.contacts["to contact name"].chat  # 1-to-1 conversation
    ch.sendMsg(partnumber + " is  stock")  # plain-text message
    call = sk.placecall("")
    print(call)

driver.close()







