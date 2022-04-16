from selenium import webdriver
import time

def pop(time_sec):
    driver = webdriver.Chrome(executable_path="C:/Users/cheekety/chromedriver_win32/chromedriver.exe")
    driver.get('https://popcat.click')
    time.sleep(2)
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        driver.find_element_by_xpath('//div[1]/div').click()
        time_sec -= 1
    else:
        driver.quit()
        
while(0<1):
    pop(33)