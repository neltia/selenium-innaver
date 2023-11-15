from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from source import verfication


# common: body page_down
def page_down(driver, idx):
    idx = int(idx)
    body = driver.find_element(By.CSS_SELECTOR, "body")
    for _ in range(idx):
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(1)


# file: get_follow_list & naver_script
# url: in.naver.com/<id>/talktalkList
# common: find unread tab element
def find_unread_element(driver):
    unread_xpath = "/html/body/div/div[1]/div/div[2]/div[2]/div[1]/button[2]"
    stat, unread_element = verfication.find_element(driver, By.XPATH, unread_xpath)
    return stat, unread_element
