import time
from selenium import webdriver
from selenium.webdriver.common.by import By

webdriverPath = ''
url = "https://www.mudah.my/malaysia/computers-and-accessories-for-sale?q=gpu"

def crawl(webdriverPath, url):
    driver = webdriver.Firefox(executable_path=f"{webdriverPath}")
    driver.get(f"{url}")
    page = 2
    time.sleep(3)
    while driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[5]/div/div[1]/ul/li[last()]").is_enabled():
        try:
            contents = scrape(driver)
            for item, price, condition, location in contents:
                print(f'{{NAME: {item}, PRICE: RM {price}, CONDITION: {condition}, LOCATION: {location} }}\n')
            driver.find_element(By.XPATH, "//div[1]/div[3]/div[5]/div/div[1]/ul/li[last()]").click()
            page += 1
            time.sleep(3)
        except:
            driver.close()
            break

def scrape(driver):
    items, prices, conditions, locations = [], [], [], []
    for item in driver.find_elements(By.XPATH, "//div[1]/div[3]/div[4]/div[1]/div/div[2]/a"):
        items.append(item.text)
    for price in driver.find_elements(By.XPATH, '//div[1]/div[3]/div[4]/div[1]/div/div[2]/div[1]/div'):
        prices.append(price.text)
    for condition in driver.find_elements(By.XPATH, "//div[1]/div[3]/div[4]/div[1]/div/div[2]/div[2]/div[1]/div"):
        conditions.append(condition.text)
    for location in driver.find_elements(By.XPATH, "//div[1]/div[3]/div[4]/div[1]/div/div[3]/div[1]/span[2]/span"):
        locations.append(location.text)
    contents = zip(items, prices, conditions, locations)
    return contents

crawl(webdriverPath,url)