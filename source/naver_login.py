from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pyperclip
import time
import json
import os


# 이미 로그인된 세션이 있는지 확인
def check_saved_session(driver):
    try:
        with open('cookie.json', 'r') as file:
            data = json.load(file)
            domain = data["url"]
            driver.get(domain)
            cookies = data["cookies"]
            # 저장된 세션을 추가
            for key, value in cookies.items():
                cookie = {"name": key, "value": value, "domain": "naver.com", "path": "/"}
                driver.add_cookie(cookie)
        return True
    except FileNotFoundError:
        return False


def cookiedump(driver, login_url):
    _cookies = driver.get_cookies()

    cookie_dict = {}
    for cookie in _cookies:
        cookie_dict[cookie['name']] = cookie['value']

    data = {'url': login_url, 'cookies': cookie_dict}
    with open('cookie.json', 'w') as f:
        json.dump(data, f, indent=2)


# 네이버: 로그인 함수
def login(driver, user_id, user_pw):
    use_login_cookie = bool(os.getenv("INMN_LOGIN_COOKIE"))
    if use_login_cookie and check_saved_session(driver):
        return

    # 1. 네이버 이동
    driver.get('https://naver.com')

    # 2. 로그인 버튼 클릭
    btn_class_name = 'MyView-module__link_login___HpHMW'
    elem = driver.find_element(By.CLASS_NAME, btn_class_name)
    elem.click()

    # 3. id 입력
    elem_id = driver.find_element(By.ID, 'id')
    elem_id.click()
    pyperclip.copy(user_id)
    elem_id.send_keys(Keys.CONTROL, 'v')
    time.sleep(1)

    # 4. pw 복사 붙여넣기
    elem_pw = driver.find_element(By.ID, 'pw')
    elem_pw.click()
    pyperclip.copy(user_pw)
    elem_pw.send_keys(Keys.CONTROL, 'v')
    time.sleep(1)

    # 5. 로그인 버튼 클릭
    driver.find_element(By.ID, 'log.login').click()
    time.sleep(3)

    if use_login_cookie:
        login_url = driver.current_url
        cookiedump(driver, login_url)
    return
