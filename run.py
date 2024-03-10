""" source의 main.py 실행 """
import argparse
from dotenv import load_dotenv
from selenium.common import exceptions
from tabulate import tabulate
import os
from source.main import main
from get_cookie_file import save_today_cookie


# python run.py <command> [opt1]
def param_parsing():
    parser = argparse.ArgumentParser(
        prog="inmn",
        description="네이버 인플루언서 및 블로그의 반복 작업을 자동화하는 프로그램입니다."
    )
    parser.add_argument(
        'command', type=str,
        choices=["follow-file", "follow-talk", "follow-follower", "read-talk"],
        help='지정된 명렁어 중 하나를 입력해 작업을 수행합니다.'
    )
    parser.add_argument(
        '-i', '--input-file', type=str, default="",
        help='작업 수행 시 파일을 전달해야 하는 경우에 사용하는 옵션입니다.',
    )
    parser.add_argument(
        '-c', '--input-excel-col', type=str, default="",
        help='작업 수행 시 엑셀 파일을 전달해야 하는 경우 중 특정 열을 지정하고 싶을 때 사용하는 옵션입니다.',
    )
    parser.add_argument(
        '-p', '--max-page', default="0",
        help='작업 수행 시 목록을 조회할 때 조회할 목록을 늘릴 수 있는 옵션입니다.',
    )
    parser.add_argument(
        '--login-cookie', action="store_true",
        help='해당 옵션 사용 시 로그인 작업을 최초 1회 수행 시 다음부터는 해당 로그인 정보를 기억하도록 합니다.',
    )
    args = parser.parse_args()
    return args


# +-- info log --+
def info_msg():
    log_info = [
        ["inmn: innaver-manage"],
        ["@neltia"],
        ["Last Version: 24.01.28"]
    ]
    table_info = tabulate(log_info, tablefmt="psql")
    return table_info


# env init & run serve
def run(command):
    # env
    load_dotenv(verbose=True)
    user_id = os.environ.get("naver_id")
    user_pw = os.environ.get("naver_pw")
    my_influencer_id = os.environ.get("my_influencer_id", "")

    # run command
    main(command, user_id, user_pw, my_influencer_id)

    return


if __name__ == '__main__':
    load_dotenv(verbose=True)
    args = param_parsing()
    command = args.command
    max_page = args.max_page
    input_excel_col = args.input_excel_col
    login_cookie = args.login_cookie

    if login_cookie:
        # 현재 날짜 네이버 로그인 쿠키 파일 탐색
        save_today_cookie()

    table_info = info_msg()
    print(table_info)

    os.environ['INMN_EXCEL_COL'] = input_excel_col
    os.environ['INMN_MAX_PAGE'] = max_page
    os.environ['INMN_LOGIN_COOKIE'] = str(login_cookie)

    try:
        run(args)
    except exceptions.NoSuchWindowException:
        print("비정상 종료되었습니다.")
