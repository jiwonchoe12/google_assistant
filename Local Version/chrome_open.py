from boilerpy3 import extractors
from selenium import webdriver
from urllib import parse
from bs4 import BeautifulSoup
import time
import json
from gpt_zero import *
from PyKakao import KoGPT

#셀레니움으로 크롬 구글웹 띄우는 부분
driver = webdriver.Chrome('/Users/choejiwon/Desktop/gpt_zero/chromedriver') #<작성1> chrome driver 경로 적기
driver.implicitly_wait(3)
driver.get('https://www.google.com')


beforeURL = ""

while True:
    #사용자가 검색한 내용(문자열) 가져오는 부분
    while True:
        if beforeURL != driver.current_url and "https://www.google.com/search?" in driver.current_url:
            title = parse.unquote(driver.current_url[driver.current_url.find("q=") + 2: driver.current_url.find("&source=")])
            beforeURL = driver.current_url
            break
        time.sleep(1)
 
    #KoGPT에게 답변을 받아오는 부분
    api = KoGPT(service_key="db9cb3efa6c03716b36859b28c6aea85") #<작성2> 발급 받은 키를 입력하기
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
            gpt_answer[i] = '*'
        i += 1
    gpt_answer = ''.join(s for s in gpt_answer)
    gpt_answer = "\\n[koGPT의 답변]\\n" + gpt_answer
    print()
    print(gpt_answer) #결과 생성
    driver.execute_script(f"""document.getElementsByClassName("NhRr3b aBOYt")[0].innerHTML += \'<div style=\"display:block\">{gpt_answer}</div>\';""")

    #gptZero 실행하는 부분
    searchDriver = webdriver.Chrome('/Users/choejiwon/Desktop/gpt_zero/chromedriver') #<작성1> chrome driver 경로 적기
    searchDriver.implicitly_wait(3)

    #html코드 가지고 와서 링크들만 추출하기
    source = driver.page_source
    soup = BeautifulSoup(source, 'html.parser')

    elements = soup.find_all('h3')

    #elements = soup.find_all('div', 'yuRUbf')
    extractor = extractors.ArticleExtractor() #boilerpipe 객체 만들기

    for element in elements:
        try:
            print(element.parent['href'])
            searchDriver.get(element.parent['href']) #url로 이동
            content = extractor.get_content(searchDriver.page_source) #각 url의 내용
            #gpt-zero 웹사이트로 api를 보내서 결과 받아오기
            if len(content) >= 50000: #내용의 길이가 길면 잘라준다
                content = content[:50000]
            gptZero_res = gptZero(content)

            try:
                jgptZero = json.loads(gptZero_res.text)
                jgptZero["documents"]
                perplexity = 0 #AI와 얼마나 근접한지의 수치
                for sentence in jgptZero["documents"][0]["sentences"]:
                    perplexity += sentence['perplexity']
                perplexity = perplexity / len(jgptZero["documents"][0]["sentences"])
                print(perplexity)
                i = elements.index(element)
                driver.execute_script(f"""document.getElementsByTagName("h3")[{i}].innerHTML = document.getElementsByTagName("h3")[{i}].innerHTML + '<font color=\"red\"> {round(perplexity,2)} </font>'""")
                print()
            except:
                print("Error Column")
        except:
            print("Error Href")
    searchDriver.close()