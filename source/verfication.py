from selenium.webdriver.common.by import By
from selenium.common import exceptions


# 해당 element가 없는 경우에 대한 공통 예외처리
# 최초 페이지 접근 시, 혹은 사이트 내부 업데이트 시 변경될 수 있음
def find_element(driver, by_key, by_value):
    try:
        element = driver.find_element(by_key, by_value)
    except exceptions.NoSuchElementException:
        return -1, None
    return 0, element


# verfication: 이미 팬하기를 한 인플루언서인가?
def is_followed(driver):
    home_div_class = "hm-component-homeCover-profile-btn"
    stat, home_div_elem = find_element(driver, By.CLASS_NAME, home_div_class)
    if stat == -1:
        msg = "해당 인플루언서를 찾을 수 없습니다."
        print(msg)
        return -1

    try:
        home_text = home_div_elem.text
    except AttributeError:
        return -1

    if "팬하기" in home_text:
        return True
    else:
        return False
