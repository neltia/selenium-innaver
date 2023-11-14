from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common import exceptions
import time
from source import verfication


# 네이버 인플루언서: 팬하기 자동화 수행
def influencer_follow(driver, influencer_list):
    follow_btn_class = "hm-component-homeCover-profile-btn"
    alert_div_class = "FanPopup__label_notice___iPdOs"
    close_btn_class = "FanPopup__button_close___rBmXm"

    for idx, influencer_id in enumerate(influencer_list):
        idx += 1
        if influencer_id.startswith("https://in.naver.com/"):
            influencer_id = influencer_id.split("/")[-1]

        page = f"https://in.naver.com/{influencer_id}"
        driver.get(page)
        time.sleep(1)

        verify = verfication.is_followed(driver)
        # - 잘못된 질의 혹은 이미 팬하기가 되어있는 경우
        if verify == -1:
            print(f"{idx} {influencer_id}: 유효하지 않은 인플루언서 아이디")
            continue
        if verify == -1:
            print(f"{idx} {influencer_id}: 이미 팬")
            continue

        msg = f"신규: {verify}"
        print(idx, influencer_id, msg)

        time.sleep(1)
        try:
            follow_elem = driver.find_element(By.CLASS_NAME, follow_btn_class)
            follow_elem.click()
            print("팬하기 완료")

            disable_elem = driver.find_element(By.CLASS_NAME, alert_div_class)
            disable_elem.click()
            close_elem = driver.find_element(By.CLASS_NAME, close_btn_class)
            close_elem.click()
            print("알림 취소 설정 완료")
        except exceptions.NoSuchElementException:
            print("네이버의 인플루언서 홈 정보가 변경되었습니다. 프로그램 버전 업데이트가 필요합니다.")
            continue
