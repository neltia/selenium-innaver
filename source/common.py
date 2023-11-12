from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


# common body page_down
def page_down(driver, idx):
    idx = int(idx)
    body = driver.find_element(By.CSS_SELECTOR, "body")
    for _ in range(idx):
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(1)
