from bs4 import BeautifulSoup
import re
import os
import time
from openpyxl import load_workbook
from source.common import page_down, find_unread_element


# 네이버 톡톡 목록 가져오기
# 네이버 톡톡 리스트에서 각 "https://in.naver.com" 링크 파싱
def talktalk(driver, my_influencer_id):
    influencer_list = list()

    talktalk_page = f"https://in.naver.com/{my_influencer_id}/talktalkList"
    driver.get(talktalk_page)
    time.sleep(1)

    # 접근 권한 확인: 전체/안읽은 탭 메뉴가 있는지 확인
    stat, unread_element = find_unread_element(driver)
    if stat == -1:
        print(f"{my_influencer_id}: 본인의 인플루언서 아이디를 입력해주세요. 접근 권한이 없습니다.")
        return influencer_list
    # 톡톡 목록 중 '안 읽음' 목록만 가져와서 '팬하기'를 사용할 것인지 선택
    # unread_element.click()

    # max_page만큼 PageDOWN 실행
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

    pat = r"(?:https:\/\/in\.naver\.com\/)(\S+)"
    influencer_id_pat = re.compile(pat, re.MULTILINE)
    influencer_list = influencer_id_pat.findall(talktalk_data)

    return influencer_list


# 따로 만든 파일에서 인플루언서 아이디 목록 가져오기
# 지원 파일: txt, excel
def read_file(file_path):
    # default follow list file path: .follow_list.txt
    if file_path == "":
        file_path = "follow_list.txt"
        msg = "-i 옵션으로 파일 경로를 지정하지 않으면 기본 'follow_list.txt' 파일을 참조합니다."
        print(msg)

    # txt
    if file_path.endswith(".txt"):
        with open(file_path, "r") as f:
            influencer_list = f.readlines()
        return influencer_list

    # excel
    if file_path.endswith(".xlsx"):
        wb = load_workbook(file_path)
        sheet_list = wb.sheetnames
        ws = wb[sheet_list[0]]

        excel_col = os.environ.get("INMN_EXCEL_COL")
        if excel_col == "":
            excel_col = "B"
            msg = "엑셀의 특정 열을 지정하지 않으면 기본 엑셀 파일의 B열을 참조합니다."
            print(msg)

        influencer_list = [cell.value for cell in ws[excel_col]]
        return influencer_list
