from selenium.webdriver.common.by import By
from selenium.common import exceptions
from bs4 import BeautifulSoup
import re
import os
from source.common import page_down


# 네이버 톡톡에서 안 읽음으로 처리된 목록 가져오기
# 네이버 톡톡 리스트에서 각 "https://in.naver.com" 링크 파싱
def talktalk(driver, my_influencer_id):
    influencer_list = list()

    talktalk_page = f"https://in.naver.com/{my_influencer_id}/talktalkList"
    driver.get(talktalk_page)

    # 안 읽음 처리된 톡톡 탭 메뉴 선택
    unread_btn_xpath = "/html/body/div/div[1]/div/div[2]/div[2]/div[1]/button[2]"
    try:
        unread_btn_xpath = driver.find_element(By.XPATH, unread_btn_xpath)
    except exceptions.NoSuchElementException:
        msg = "본인의 인플루언서 아이디를 입력해주세요. 접근 권한이 없습니다."
        print(msg)
        return influencer_list

    max_page = os.environ.get("INMN_MAX_PAGE")
    page_down(driver, max_page)

    # 톡톡 리스트에서 "https://in.naver.com" 링크 파싱
    page_html = driver.page_source
    soup = BeautifulSoup(page_html, "lxml")
    link_class_name = "TalkTalkList__ell___anpyL"
    talktalk_list = soup.find_all("span", attrs={"class": link_class_name})

    talktalk_data = ""
    for idx in range(0, len(talktalk_list), 2):
        # influencer_name = talktalk_list[idx].text
        talktalk = talktalk_list[idx+1].text
        talktalk_data += f"{talktalk}\n"

    pat = r"(?:https:\/\/in\.naver\.com\/)(\w+)"
    influencer_id_pat = re.compile(pat, re.MULTILINE)
    influencer_list = influencer_id_pat.findall(talktalk_data)

    return influencer_list


# 따로 만든 파일에서 인플루언서 아이디 목록 가져오기
# 지원 파일: txt, excel
def read_file(file_path):
    influencer_list = list()
    return influencer_list
