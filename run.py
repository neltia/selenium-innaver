""" source의 main.py 실행 """
import argparse
from dotenv import load_dotenv
from selenium.common import exceptions
from tabulate import tabulate
import os
from source.main import main


# python run.py <command> [opt1]
def param_parsing():
    parser = argparse.ArgumentParser(
        prog="inmn",
        description="네이버 인플루언서 및 블로그의 반복 작업을 자동화하는 프로그램입니다."
    )
    parser.add_argument(
        'command', type=str,
        help='지정된 명렁어 중 하나를 입력해 작업을 수행합니다.'
    )
    parser.add_argument(
        '-i', '--input-file', type=str, default="",
        help='작업 수행 시 파일을 전달해야 하는 경우에 사용하는 옵션입니다.',
    )
    parser.add_argument(
        '-p', '--max-page', default=0,
        help='작업 수행 시 목록을 조회할 때 조회할 목록을 늘릴 수 있는 옵션입니다.',
    )
    args = parser.parse_args()
    return args


# +-- info log --+
def info_msg(command):
    log_info = [
        ["inmn: innaver-manage"],
        [f"command: <{command}>"],
        ["@neltia"],
        ["Last Modified: 23.11.12"]
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

    table_info = info_msg(args)
    print(table_info)

    os.environ['INMN_MAX_PAGE'] = max_page
    try:
        run(args)
    except exceptions.NoSuchWindowException:
        print("비정상 종료되었습니다.")