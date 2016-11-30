from selenium import webdriver
from selenium.webdriver.common.keys import Keys

print "ComEd Scraper"
url = "https://secure.comed.com/MyAccount/MyService/Pages/UsageDataTool.aspx"
driver = webdriver.Chrome('/Users/akmoore8798/chromedriver')
driver.get(url)
button = driver.find_element_by_xpath('//*[@id="ctl00_ctl76_g_86daaf10_fb31_4f6d_adf3_d7c384f128a3_ctl00_RequestOption_0"]')
button.click()
textField = driver.find_element_by_xpath('//*[@id="AccountNumber"]')
textField.send_keys("**********")
addButton = driver.find_element_by_xpath('//*[@id="ctl00_ctl76_g_86daaf10_fb31_4f6d_adf3_d7c384f128a3_ctl00_Addbtn"]')
addButton.click()
csvFile = driver.find_element_by_xpath('//*[@id="ctl00_ctl76_g_86daaf10_fb31_4f6d_adf3_d7c384f128a3_ctl00_Downloadbtn"]')
csvFile.click()
