from source.driver_settings import get_driver
from source import naver_login
from source import naver_script
from source import get_follow_list


# 메인 함수
def main(args, user_id, user_pw, my_influencer_id):
    driver = get_driver()
    naver_login.login(driver, user_id, user_pw)

    command = args.command

    """ 네이버 인플루언서 팬하기 """
    # follow-file: txt, excel 등 파일에 적힌 리스트를 기반으로 팬하기 리스트 생성
    if command == "follow-file":
        input_file = args.input_file
        influencer_list = get_follow_list.read_file(input_file)
    # follow-talk: 네이버 톡톡에 온 톡톡 목록을 기반으로 팬하기 리스트 생성
    elif command == "follow-talk":
        influencer_list = get_follow_list.talktalk(driver, my_influencer_id)
    # 파일 기반과 톡톡 기반 말고도 여러 기준이 있을 수 있음
    # 해당 내용을 포괄해 리스트에 있는 내용을 따라 팬하기 자동화 작업 수행
    if command.startswith("follow"):
        naver_script.influencer_follow(driver, influencer_list)

    return
