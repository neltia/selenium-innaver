from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common import exceptions
import os
import time
from source.common import page_down, find_unread_element
from source import verfication


# <List> 네이버 인플루언서: 팬하기 자동화 수행
def influencer_follow(driver, influencer_list):
    for idx, influencer_id in enumerate(influencer_list):
        idx += 1
        print(f"{idx}. start")

        if influencer_id.startswith("https://in.naver.com/"):
            influencer_id = influencer_id.split("/")[-1]

        res_code = influencer_follow_one(driver, influencer_id)
        if res_code == -1:
            continue


# 네이버 인플루언서: 팬하기 자동화 수행
def influencer_follow_one(driver, influencer_id):
    btn_div_class = "hm-component-homeCover-profile-btn"
    alert_div_class = "FanPopup__label_notice___iPdOs"
    close_btn_class = "FanPopup__button_close___rBmXm"

    page = f"https://in.naver.com/{influencer_id}"
    driver.get(page)
    time.sleep(1)

    verify = verfication.is_followed(driver)
    # - 잘못된 질의 혹은 이미 팬하기가 되어있는 경우
    if verify == -1:
        print(f"{influencer_id}: 유효하지 않은 인플루언서 아이디")
        return -1
    if not verify:
        print(f"{influencer_id}: 이미 팬")
        return -1

    msg = f"신규: {verify}"
    print(influencer_id, msg)

    time.sleep(1)
    try:
        follow_dim = driver.find_element(By.CLASS_NAME, btn_div_class)
        follow_elem = follow_dim.find_element(By.TAG_NAME, "button")
        follow_elem.click()
        print("팬하기 완료")

        disable_elem = driver.find_element(By.CLASS_NAME, alert_div_class)
        disable_elem.click()
        close_elem = driver.find_element(By.CLASS_NAME, close_btn_class)
        close_elem.click()
        print("알림 취소 설정 완료")
        return 0
    except exceptions.NoSuchElementException:
        print("네이버의 인플루언서 홈 정보가 변경되었습니다. 프로그램 버전 업데이트가 필요합니다.")
        return -1


# 네이버: 네이버 톡톡 읽음 처리
def talk_noti(driver, my_influencer_id):
    talktalk_url = f"https://in.naver.com/{my_influencer_id}/talktalkList"
    driver.get(talktalk_url)
    time.sleep(1)

    # 안읽음 탭 선택
    stat, unread_element = find_unread_element(driver)
    if stat == -1:
        print(f"{my_influencer_id}: 본인의 인플루언서 아이디를 입력해주세요. 접근 권한이 없습니다.")
        return
    unread_element.click()

    # max_page만큼 PageDOWN 실행
    max_page = os.environ.get("INMN_MAX_PAGE")
    page_down(driver, max_page)

    # 안 읽은 톡톡 목록을 가져옴
    link_class_name = "TalkTalkList__ell___anpyL"
    talktalk_list = driver.find_elements(By.CLASS_NAME, link_class_name)
    if len(talktalk_list) == 0:
        msg = "안 읽은 톡톡 메시지가 없습니다."
        print(msg)
        return

    # 개별 톡톡 클릭 후 돌아가기
    for _ in range(len(talktalk_list)):
        talk = driver.find_element(By.CLASS_NAME, link_class_name)
        try:
            talk.click()
        except (AttributeError, exceptions.NoSuchElementException):
            break
        driver.back()
        time.sleep(1)

        stat, unread_element = find_unread_element(driver)
        unread_element.click()
        time.sleep(1)

    return


# 네이버: 톡톡 메시지 보내기
def send_talk(driver):
    btn_class = "hm-component-homeCover-profile-btn"
    btn_box = driver.find_element(By.CLASS_NAME, btn_class)

    # 톡톡 메시지를 허용하지 않은 인플루언서도 있음
    try:
        talk_btn = btn_box.find_elements(By.TAG_NAME, "button")[1]
    except (exceptions.ElementNotInteractableException, KeyError):
        print("맞팬 요청 톡톡 메시지 전송 실패")
        return -1

    talk_btn.click()
    time.sleep(3)

    with open("talktalk_msg.txt", "r", encoding="utf-8") as f:
        data = f.read()

    chat_input_class = "chat_input"
    chat_input = driver.find_element(By.CLASS_NAME, chat_input_class)
    chat_input.send_keys(data)

    time.sleep(1)
    print("맞팬 요청 톡톡 메시지 전송 완료")

    return 0
