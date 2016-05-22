import random
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

THANK_YOU_MESSAGES = ["Thanks! :D",
                      "Thank you so much!",
                      "Thanks a lot :)",
                      "Thanks a ton! :D",
                      "Thank you! :)"]

driver = webdriver.Firefox()
driver.maximize_window()
driver.get('https://www.facebook.com')
assert "Facebook" in driver.title
elem = driver.find_element_by_id("email")
elem.send_keys("dumpsmtp@gmail.com")
elem = driver.find_element_by_id("pass")
elem.send_keys("seleniumrocks!")
elem.send_keys(Keys.RETURN)

elem = driver.find_element_by_xpath("//a[@title='Profile']")
elem.click()

# for elem in driver.find_elements_by_css_selector("a[class^='UFILikeLink']"):
#     elem.click()
time.sleep(5)
comments = driver.find_elements_by_css_selector("div[class^='UFIAddCommentInput']")
total = len(comments)


for index in range(0, total):
	driver.get("https://www.facebook.com/profile.php?id=100012234069444")
	driver.execute_script("window.scrollBy(0, "+str(200*index)+");")
	comments = driver.find_elements_by_css_selector("div[class^='UFIAddCommentInput']")
	print comments
	elem = comments[index]
	print elem
	# driver.execute_script("return arguments[0].scrollIntoView();", elem)
	elem.click()
	element = driver.find_element_by_class_name("_5rpu")
	element.send_keys(random.choice(THANK_YOU_MESSAGES))
	element.send_keys(Keys.RETURN)
