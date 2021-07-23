from selenium import webdriver
import time

def scraper(username, password):

	'''
	for headless options use these lines of code 
	'''
	#fireFoxOptions = webdriver.FirefoxOptions()
	#fireFoxOptions.set_headless()
	#driver = webdriver.Firefox(firefox_options=fireFoxOptions)

	'''
	normal options with UI showing
	'''
	driver = webdriver.Firefox()
	driver.get('https://www.ptptn.gov.my/ionline/#/login')
	time.sleep(3) # Wait for website to load
	driver.find_element_by_xpath('//ion-app/ng-component/ion-split-pane/ion-nav/page-login/ion-content/div[2]/form/ion-list/ion-item[1]/div[1]/div/ion-input/input').send_keys(username)
	driver.find_element_by_xpath('//ion-app/ng-component/ion-split-pane/ion-nav/page-login/ion-content/div[2]/form/ion-list/ion-item[2]/div[1]/div/ion-input/input').send_keys(password)
	driver.find_element_by_xpath('//ion-app/ng-component/ion-split-pane/ion-nav/page-login/ion-content/div[2]/form/ion-row/ion-col[1]/button').click()
	time.sleep(2)
	driver.find_element_by_xpath('//ion-app/ng-component/ion-split-pane/ion-menu[1]/div/ion-content/div[2]/ion-list[1]/div/button[7]').click()
	driver.switch_to_window(driver.window_handles[1]) # Switch to active window
	time.sleep(5)
	total_debt = driver.find_element_by_xpath('//div/div/div[2]/div[2]/table/tfoot/tr/td[6]').text
	driver.quit()
	print(f'Total debt: RM{total_debt}')

scraper('username_here', 'password_here')
