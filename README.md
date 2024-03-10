# 네이버 인플루언서 홈(in.naver.com) 관리 도구
## 프로젝트 배경
<strong>네이버 인플루언서 홈이란?</strong>
- https://in.naver.com/intro
<p>
    네이버 블로그, 유튜브, 인스타그램 등 플랫폼을 운영하는 사람들은 네이버의 인플루언서 홈에 '인플루언서'로 신청할 수 있습니다.
</p>
<p>
    운영 중인 플랫폼의 조회수나 구독자 수 등 지표를 가지고 심사해 '인플루언서'로 통과가 되면 네이버의 인플루언서 홈을 개설하여 여러 플랫폼을 운영 중이라면 한 곳에서 모아볼 수 있습니다.
</p>

<strong>"팬하기" 관리의 필요성</strong>
<p>
    특히 네이버 블로그를 운영하는 네이버 블로거는 작성한 글의 검색 순위에도 영향을 받아 '애드포스트'의 광고 수익으로도 이어집니다.
</p>
<p>
    네이버 블로그를 운영 중인 일반 블로거보다 '인플루언서'로 선정된 '인플루언서' 네이버 블로거의 검색 순위가 기본적으로 높게 설정되고, 그 중에서도 '인플루언서'의 '팬' 수에 따라 상위에 노출될 확률이 커집니다.
</p>
<p>
    이에 '인플루언서'인 사람들끼리 서로 '팬하기'를 눌러주는 '맞팬'의 방식으로 '팬'수를 늘리면서, 자동화해주는 매크로 프로그램을 사용하기까지 하지만, 전공자가 아닌 대부분은 일정 기간 사용하는 것을 전제로 유료에 프로그램을 구매해서 사용하는 편입니다.
</p>
<p>
    우선순위가 밀려 필요했으나 개발을 미뤘는데, 일단은 내가 사용하고자 미니 프로젝트 차원에서 시작합니다.
</p>

## 프로젝트 소개
<strong>프로그램 사용 대상</strong>
- 네이버 인플루언서 홈에 등록된 '팬' 수를 늘리고 싶은 인플루언서

<strong>주요 기능</strong>
<p>
    다음과 같은 기능들을 파이썬 스크립트 프로그램이나 Tkinter GUI 프로그램으로 조작
</p>
- 네이버 자동 로그인
- '팬하기' 대상 목록 만들기
    - 본인의 네이버 톡톡에 들어오는 맞팬 신청에 대해 자동으로 '팬하기' 대상 리스팅
    - 주어진 파일(txt, xlsx)을 기반으로 '팬하기' 대상 리스팅
    - 추가1. 먼저 '맞팬'을 신청할 '팬하기' 대상 인플루언서를 탐색해서 리스팅
    - 추가2. sqlite3를 가지고 이미 팬하기를 한 대상은 리스트에서 스킵해서 넘어갈 수 있도록 구성
- '팬하기' 대상 목록을 기반으로 자동 "팬하기" 신청
    - '팬하기' 신청 시 네이버 알림 해제 기능
- 네이버 톡톡 대화목록 읽음 처리
- 네이버 서로이웃 자동 신청

## 개발 환경
lang: Python 3.6+
lib ver.
<pre>
python-dotenv==0.21.1
pyperclip==1.8.2
beautifulsoup4==4.11.2
selenium==4.8.2
openpyxl==3.1.2
</pre>

## 도움말
<p>자동 쿠키 추출 기능을 사용하려면 로컬에 있는 크롬 드라이버 위치 값을 넣어야 함</p>

- driver_settings.py: driver_path 값 변경

<pre>
def get_driver_debug():
    options = Options()
    options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

    # driver abs path
    # 1. 파일 탐색기 열기(Win + E)
    # 2. chromedriver.exe 검색
    # 3. 파일 위치를 열어 해당 크롬 드라이버를 열어 네이버 로그인까지 선행
    # example path. C:\\Users\USERNAME\\.wdm\drivers\\chromedriver\win64\\122.0.6261.95\\chromedriver-win32\\chromedriver.exe

    driver_path = ""
</pre>

- 참고. cmd 열어 드라이버 실행

<pre>
    cd  C:\Program Files\Google\Chrome\Application
    chrome.exe --remote-debugging-port=9222 --user-data-dir=
</pre>
