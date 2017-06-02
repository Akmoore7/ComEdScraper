from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime
from selenium.webdriver.chrome.options import Options
import time
import pandas
import shutil
import os
import os.path
import sys


def downCSV( accnNum ):
	url = "https://secure.comed.com/MyAccount/MyService/Pages/UsageDataTool.aspx"
	driver = webdriver.Chrome('LOCATION OF CHROME DRIVER')
	try:
		driver.set_window_size(200, 100)
		driver.set_page_load_timeout(20.0)
                driver.get(url)
		button = driver.find_element_by_id('ctl00_ctl76_g_86daaf10_fb31_4f6d_adf3_d7c384f128a3_ctl00_RequestOption_0')
		button.click()
		textField = driver.find_element_by_id('AccountNumber')
		textField.send_keys(accnNum)
		addButton = driver.find_element_by_id('ctl00_ctl76_g_86daaf10_fb31_4f6d_adf3_d7c384f128a3_ctl00_Addbtn')
		addButton.click()
		csvFile = driver.find_element_by_id('ctl00_ctl76_g_86daaf10_fb31_4f6d_adf3_d7c384f128a3_ctl00_Downloadbtn')
		csvFile.click()
		time.sleep(1.0)
		driver.quit()
	except:
                print("Load Fail")
		driver.quit()

def grabAccNums():
	fields = ['Account_Number']
	accNums = pandas.read_csv('LIST OF ACCOUNT NUMBERS TO BE SCRAPED', usecols=fields)
	return(accNums)

## MAIN?
#file = open('/Users/alexmoore/Python/tempFaulty.txt', 'a')
file = open('LOCATION OF FILE WHERE FAULTY ACCOUNTS ARE STORED', 'a')
accNums = grabAccNums()
start = int(sys.argv[1])
end = int(sys.argv[2])
print("START: " + str(start))
print("END: " + str(end))
for i in range(start, end):
	downCSV(accNums.Account_Number[i])
	exists = os.path.isfile('CHECKS IF SUMMARYUSAGEDATA.ZIP EXISTS IN DOWNLOADS')
	if exists:
		stringAccount = str(accNums.Account_Number[i]) + '.zip'
		#shareName = '/Users/alexmoore/Python/TempComEdScraperData/' + stringAccoun
		shareName = '/Volumes/share/projects/ARRA/store/ComEdScraperData/' + stringAccount
		shutil.move('/Users/Downloads/SummaryUsageData.zip', shareName)
		print(accNums.Account_Number[i])
	else:
	        print(accNums.Account_Number[i]+ "  FAIL")
		file.write(str(accNums.Account_Number[i]) + "\n")
	        file.close()
		file = open('/Volumes/share/projects/ARRA/store/FaultyAccounts.txt', 'a')
                #file = open('/Users/Python/tempFaulty.txt', 'a')
file.close()
