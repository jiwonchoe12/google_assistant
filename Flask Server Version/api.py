from flask import Flask # Flask 모듈이 추가 -> Api 제작을 위한 모듈
import flask
import json
from boilerpy3 import extractors
from selenium import webdriver
from gpt_zero import *
from PyKakao import KoGPT

app = Flask (__name__) # Flask 객체를 하나 만든다.

@app.route('/title/<title>')
def kogpt_answer(title):
    print(title)
    api = KoGPT(service_key="db9cb3efa6c03716b36859b28c6aea85") #<작성1> 발급받은 키 입력
    prompt = title
    max_tokens = 128
    result = api.generate(prompt, max_tokens, temperature=0.2)
    print(result)
    gpt_answer = str(result['generations'])
    gpt_answer = gpt_answer[11:-18]
    gpt_answer = list(gpt_answer)
    
    i = 0
    while i < len(gpt_answer):
        if gpt_answer[i] == '\"' or gpt_answer[i] == '\'':
            gpt_answer[i] = ''
        i += 1
    gpt_answer = ''.join(s for s in gpt_answer)
    gpt_answer = "[koGPT의 답변]" + gpt_answer
    print(gpt_answer) #결과 생성
    my_res = flask.Response(str(gpt_answer)) # 구한 결과를 flask 답변 형식으로 변환한다. | 이유는 CORS 규정 위반을 해결하기 위해서 변환했다.
    my_res.headers["Access-Control-Allow-Origin"] = "*" # CORS 규정 에러를 해결하기 위해 추가된 코드 (헤더에 추가)
    return my_res


@app.route('/api/<url>') # URL뒤에 <>을 이용해 가변 경로를 적는다
def hello_user(url): # url은 요청에서 들어온 주소
    url = url.replace('~', '/') # 치환된 ~을 /로 복구
    print(url)
    url = "https://" + url
    driver.get(url) # 셀레니움에 해당 주소 이동.
    content = extractor.get_content(driver.page_source) #각 url의 내용 | 이동한 url의 html코드를 받아온다. (보일러 파이프 활용)
    if len(content) >= 50000: #내용의 길이가 길면 잘라준다
        content = content[:50000]
    gptZero_res = gptZero(content) # Gpt Zero한테 결과를 얻어온다.
    perplexity = -1 # 초기값을 -1로 세팅 | 에러인 경우에는 -1
    try: # GPT Zero의 답변을 Json형식으로 파싱
        jgptZero = json.loads(gptZero_res.text)
        jgptZero["documents"]
        perplexity = 0 #AI와 얼마나 근접한지의 수치
        for sentence in jgptZero["documents"][0]["sentences"]:
            perplexity += sentence['perplexity']
        perplexity = perplexity / len(jgptZero["documents"][0]["sentences"])
        print(perplexity)
    except:
            print("Error Column")
    my_res = flask.Response(str(perplexity)) # 구한 결과를 flask 답변 형식으로 변환한다. | 이유는 CORS 규정 위반을 해결하기 위해서 변환했다.
    my_res.headers["Access-Control-Allow-Origin"] = "*" # CORS 규정 에러를 해결하기 위해 추가된 코드 (헤더에 추가)
    return my_res
 
if __name__ == "__main__":
    driver = webdriver.Chrome('/Users/choejiwon/Desktop/gpt_zero/chromedriver') #<작성2> chromedriver 경고 입력
    driver.implicitly_wait(3)
    extractor = extractors.ArticleExtractor() #boilerpipe 객체 만들기
    app.run() # Flask 실행
