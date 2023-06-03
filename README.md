# google_assistant
KoGPT와 GPTZero 를 활용한 구글 검색 어시스턴트 제작

## 🖥️ 프로젝트 소개
구글 검색 엔진에서 검색한 내용에 대한 KoGPT 답변과 각 게시물의 GPT 의존성을 확인할 수 있는 구글 검색 어시스턴트이다.
<br>

## 🕰️ 개발 기간
* 23.04.13일 - 23.06.07일

## 🧩 프로젝트 버전
- Local Version
구글 검색 어시스턴트를 로컬에서 사용하는 버전이다
- Flask Server Version
외부에서 구글 검색 어시스턴트를 사용할 수 있도록 Flask 웹서버와 자바스크립트를 제공한다

## 📌 사용자 가이드
#### 환경 구축
- GitHub Repository을 로컬 컴퓨터내에 clone한다
- “pip install -r requirements.txt”명령어로 프로그램 작동에 필요한 패키지를 설치한다

#### Local version 
1. Localversiondirectory내 chrome_open.py 파일의 11과 49번째 줄에는 chromedriver을 설치한 경로를 입력한다.
2. Kakao Developers 에서 애플리케이션 추가하기 버튼을 눌러 Rest API 키를 생성한다. 
3. 28 번째 줄에는 KoGPT 에서 발급받은 키를 입력한다.
4. 이후 프로그램을 실행한다.

#### Flask Sever version
1. Flask Server version directory 내 api.py 파일의 62 번째 줄에 chrome driver 을 설치한 경로를 입력한다.
2. Kakao Developers 에서 애플리케이션 추가하기 버튼을 눌러 Rest API 키를 생성한다. 
3. 14 번째 줄에는 KoGPT 에서 발급받은 키를 입력한다.
4. Flask Server version 은 api.py 프로그램을 서버에다가 돌린다.(로컬 컴퓨터로 진행 가능)
5. 구글에서 JavaScript 을 실행시키면 동작한다. JavaScript 을 간편하게 실행시키기 위해 코드를 북마크에다 등록한다.
- JavaScript 코드를 압축한다. 이 웹사이트를 이용한다(http://javascriptcompressor.com)
- 압축된 스크립트를 uri 문자로 인코딩 하고 javascript: 문구를 삽입하여 북마클립용 자바스크립트 코드를 만든다. 이 웹사이트를 이용 (https://nuknukhan.tistory.com/54)
- 구글의 북마크 > 북마크 관리자 > 새 북마크 추가로 이동한다
- 자바스크립트 북마크를 입력한다.
6. 북마크를 클릭하여 실행한다.
