from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


# driver setting
def get_driver():
    # 드라이버 설정
    options = Options()
    user_agent = "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Whale/3.23.214.10 Safari/537.36"
    options.add_argument(user_agent)
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")

    # 드라이버 시작
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    # 웹 페이지를 5초 안에 load되면 넘어가고, 아니면 5초 기다림
    driver.implicitly_wait(5)
    return driver


# driver setting (debug mode)
def get_driver_debug():
    options = Options()
    options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

    # driver abs path
    # 1. 파일 탐색기 열기(Win + E)
    # 2. chromedriver.exe 검색
    # 3. 파일 위치를 열어 해당 크롬 드라이버를 열어 네이버 로그인까지 선행
    # example path. C:\\Users\USERNAME\\.wdm\drivers\\chromedriver\win64\\122.0.6261.95\\chromedriver-win32\\chromedriver.exe
    driver_path = ""
    driver = webdriver.Chrome(driver_path, options=options)
    driver.implicitly_wait(5)
    return driver
