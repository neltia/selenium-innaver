from source.driver_settings import get_driver_debug
from source.naver_login import delete_cookie_files
from source.naver_login import cookiedump
from source.naver_login import get_cookie_filename
import os


def is_totay_cookie():
    filename = get_cookie_filename()
    return os.path.isfile(filename)


def save_today_cookie():
    if is_totay_cookie():
        return

    driver = get_driver_debug()
    get_url = "https://naver.com"
    nid_url = "https://nid.naver.com/login"
    driver.get(get_url)

    delete_cookie_files()
    cookiedump(driver, nid_url)


if __name__ == '__main__':
    save_today_cookie()
