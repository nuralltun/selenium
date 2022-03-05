from selenium import webdriver

from time import sleep

driver1 = webdriver.Chrome(executable_path="chromedriver")
driver2 = webdriver.Chrome(executable_path="chromedriver")
driver3 = webdriver.Chrome(executable_path="chromedriver")
driver4 = webdriver.Chrome(executable_path="chromedriver")

driver1.get("https://youtu.be/coZbOM6E47I")
driver2.get("https://youtu.be/jESNOSCLqS0")
driver3.get("https://youtu.be/0eeq0A6rc_E")
driver4.get("https://www.youtube.com/feed/explore")

while True:
    sleep(10)
    driver1.refresh()
    driver2.refresh()
    driver3.refresh()
    driver4.refresh()