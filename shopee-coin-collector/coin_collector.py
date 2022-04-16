from selenium import webdriver
import schedule
import time

def get_coins():
    driver = webdriver.Chrome(executable_path="path_to_driver/chromedriver.exe")
    driver.get('https://shopee.com.my/buyer/login')
    driver.find_element_by_xpath('//*[@id="modal"]/div[1]/div[1]/div/div[3]/div[1]/button').click()
    driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div/div/form/div/div[2]/div[2]/div[1]/input').send_keys('USERNAME')
    driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div/div/form/div/div[2]/div[3]/div[1]/input').send_keys('PASSWORD')
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div/div/form/div/div[2]/button').click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div/div/div/div[1]/div/div[2]/div[1]/button').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/main/form/div[2]/input').send_keys('CODE')
    driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/main/form/button').click()
    time.sleep(3)
    driver.get("https://shopee.com.my/shopee-coins/")
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="main"]/div/div[3]/div/main/section[1]/div[1]/button').click()
    time.sleep(3)
    driver.quit()

schedule.every().day.at("10:00").do(get_coins)

while True:
    schedule.run_pending()
    time.sleep(1)
