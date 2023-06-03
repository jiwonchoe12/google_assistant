import requests

def gptZero(data):
    cookies = {
        'cf_clearance': '2tqzVtfu08cTtVFCSBIdBoN33qGzq.Ggqj4fvuaPyD0-1682157725-0-160',
        'AMP_MKTG_8f1ede8e9c': 'JTdCJTIycmVmZXJyZXIlMjIlM0ElMjJodHRwcyUzQSUyRiUyRmdwdHplcm8ubWUlMkYlM0ZfX2NmX2NobF90ayUzRDZwMWZVUzlNODhwVXJfZGdxOEh6RjNMZ0w3YzlmTzZ5U01yZ3N6QnloYWstMTY4MjE1NzcyNS0wLWdhTnljR3pOQ3ZzJTIyJTJDJTIycmVmZXJyaW5nX2RvbWFpbiUyMiUzQSUyMmdwdHplcm8ubWUlMjIlN0Q=',
        'accessToken4': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJhdXRoZW50aWNhdGVkIiwiZXhwIjoxNjgyNzYyNTUxLCJzdWIiOiIzZTkzMTg2NC0zNWQwLTRhODEtOGNkYi05M2QwY2NhOWM0YTciLCJlbWFpbCI6ImVoYWwzNzI3QGdtYWlsLmNvbSIsInBob25lIjoiIiwiYXBwX21ldGFkYXRhIjp7InByb3ZpZGVyIjoiZ29vZ2xlIiwicHJvdmlkZXJzIjpbImdvb2dsZSJdfSwidXNlcl9tZXRhZGF0YSI6eyJhdmF0YXJfdXJsIjoiaHR0cHM6Ly9saDMuZ29vZ2xldXNlcmNvbnRlbnQuY29tL2EvQUdObXl4YVhfRkg2RDBOM0IzaElDdERfZXdFM3lMZ2J1QS1BVlp3eVNsNVc9czk2LWMiLCJlbWFpbCI6ImVoYWwzNzI3QGdtYWlsLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJmdWxsX25hbWUiOiLstZzsp4Dsm5AiLCJpc3MiOiJodHRwczovL3d3dy5nb29nbGVhcGlzLmNvbS91c2VyaW5mby92Mi9tZSIsIm5hbWUiOiLstZzsp4Dsm5AiLCJwaWN0dXJlIjoiaHR0cHM6Ly9saDMuZ29vZ2xldXNlcmNvbnRlbnQuY29tL2EvQUdObXl4YVhfRkg2RDBOM0IzaElDdERfZXdFM3lMZ2J1QS1BVlp3eVNsNVc9czk2LWMiLCJwcm92aWRlcl9pZCI6IjExNTE2ODg1MzU2ODQzNTE0ODUyMyIsInN1YiI6IjExNTE2ODg1MzU2ODQzNTE0ODUyMyJ9LCJyb2xlIjoiYXV0aGVudGljYXRlZCIsImFhbCI6ImFhbDEiLCJhbXIiOlt7Im1ldGhvZCI6Im9hdXRoIiwidGltZXN0YW1wIjoxNjgyMTU3NzUxfV0sInNlc3Npb25faWQiOiJlNjU1YzY4ZS1jMTgxLTRkNGQtOTZjMC1mYWE1YzdmM2RmMDEifQ.bCwzaa9KCgk4KwrpxzHVcyykGD_JwYxGCvmAydyw8e8',
        'AMP_8f1ede8e9c': 'JTdCJTIyZGV2aWNlSWQlMjIlM0ElMjIwZGM0MzI1Zi03ZDZiLTRmYjUtOTUzNy04YWEyNTExYjQxOGUlMjIlMkMlMjJzZXNzaW9uSWQlMjIlM0ExNjgyMTU3NzI5NTQ2JTJDJTIyb3B0T3V0JTIyJTNBZmFsc2UlMkMlMjJsYXN0RXZlbnRUaW1lJTIyJTNBMTY4MjE1Nzc4MDc5MSU3RA==',
    }

    headers = {
        'authority': 'api.gptzero.me',
        'accept': '*/*',
        'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json',
        # 'cookie': 'cf_clearance=2tqzVtfu08cTtVFCSBIdBoN33qGzq.Ggqj4fvuaPyD0-1682157725-0-160; AMP_MKTG_8f1ede8e9c=JTdCJTIycmVmZXJyZXIlMjIlM0ElMjJodHRwcyUzQSUyRiUyRmdwdHplcm8ubWUlMkYlM0ZfX2NmX2NobF90ayUzRDZwMWZVUzlNODhwVXJfZGdxOEh6RjNMZ0w3YzlmTzZ5U01yZ3N6QnloYWstMTY4MjE1NzcyNS0wLWdhTnljR3pOQ3ZzJTIyJTJDJTIycmVmZXJyaW5nX2RvbWFpbiUyMiUzQSUyMmdwdHplcm8ubWUlMjIlN0Q=; accessToken4=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJhdXRoZW50aWNhdGVkIiwiZXhwIjoxNjgyNzYyNTUxLCJzdWIiOiIzZTkzMTg2NC0zNWQwLTRhODEtOGNkYi05M2QwY2NhOWM0YTciLCJlbWFpbCI6ImVoYWwzNzI3QGdtYWlsLmNvbSIsInBob25lIjoiIiwiYXBwX21ldGFkYXRhIjp7InByb3ZpZGVyIjoiZ29vZ2xlIiwicHJvdmlkZXJzIjpbImdvb2dsZSJdfSwidXNlcl9tZXRhZGF0YSI6eyJhdmF0YXJfdXJsIjoiaHR0cHM6Ly9saDMuZ29vZ2xldXNlcmNvbnRlbnQuY29tL2EvQUdObXl4YVhfRkg2RDBOM0IzaElDdERfZXdFM3lMZ2J1QS1BVlp3eVNsNVc9czk2LWMiLCJlbWFpbCI6ImVoYWwzNzI3QGdtYWlsLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJmdWxsX25hbWUiOiLstZzsp4Dsm5AiLCJpc3MiOiJodHRwczovL3d3dy5nb29nbGVhcGlzLmNvbS91c2VyaW5mby92Mi9tZSIsIm5hbWUiOiLstZzsp4Dsm5AiLCJwaWN0dXJlIjoiaHR0cHM6Ly9saDMuZ29vZ2xldXNlcmNvbnRlbnQuY29tL2EvQUdObXl4YVhfRkg2RDBOM0IzaElDdERfZXdFM3lMZ2J1QS1BVlp3eVNsNVc9czk2LWMiLCJwcm92aWRlcl9pZCI6IjExNTE2ODg1MzU2ODQzNTE0ODUyMyIsInN1YiI6IjExNTE2ODg1MzU2ODQzNTE0ODUyMyJ9LCJyb2xlIjoiYXV0aGVudGljYXRlZCIsImFhbCI6ImFhbDEiLCJhbXIiOlt7Im1ldGhvZCI6Im9hdXRoIiwidGltZXN0YW1wIjoxNjgyMTU3NzUxfV0sInNlc3Npb25faWQiOiJlNjU1YzY4ZS1jMTgxLTRkNGQtOTZjMC1mYWE1YzdmM2RmMDEifQ.bCwzaa9KCgk4KwrpxzHVcyykGD_JwYxGCvmAydyw8e8; AMP_8f1ede8e9c=JTdCJTIyZGV2aWNlSWQlMjIlM0ElMjIwZGM0MzI1Zi03ZDZiLTRmYjUtOTUzNy04YWEyNTExYjQxOGUlMjIlMkMlMjJzZXNzaW9uSWQlMjIlM0ExNjgyMTU3NzI5NTQ2JTJDJTIyb3B0T3V0JTIyJTNBZmFsc2UlMkMlMjJsYXN0RXZlbnRUaW1lJTIyJTNBMTY4MjE1Nzc4MDc5MSU3RA==',
        'origin': 'https://app.gptzero.me',
        'referer': 'https://app.gptzero.me/',
        'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    }

    json_data = {
        'document': f'{data}',
    }

    response = requests.post('https://api.gptzero.me/v2/predict/text', cookies=cookies, headers=headers, json=json_data)
    return response

    # Note: json_data will not be serialized by requests
    # exactly as it was in the original request.
    #data = '{"document":"\\n\\n<My recommendation>\\n\\nInternet, game, graphic, music, video files\\n\\n1. Cpu part\\n3번이 가장 좋음, \\nCpu 클록 속도가 높을수록 빠르다 -> 연산 속도가 빠름\\n1, 2 번은 배터리로 동작하기 때문에 성능보다는 전력 효율에 초점이 맞춰져서 성능이 좋지 않다.\\n그와 반면에 3번은 데스크탑이니까 성능에 초점이 맞춰져 있다.따라서 우리가 필요한 고사양의 작업을 하려면 3번을 선택하는것이 좋다.\\n\\n2. Ram (memory) part\\n첫번째꺼는 1GB, 2 -> 2, 3 -> 3\\nMultitasking 능력이 좋음, 게임이나 영상을 다루는 소프트웨어는 최소 필요한 램 용량이 크다. 따라서 큰 램을 사용해야한다.\\n\\n3. Harddisk part\\n1 -> 80GB, 2->200GB\\n용량이 큰것이 좋음 -> 3번이 1TB로 크다\\n\\n4. Screen part\\n크기가 큰게 중요하면 3번, 게임을 하거나 그래픽 작업을 하면 멀티테스킹 작업을 하는데 한 창에 여러가지 프로그램을 띄워나야 하니까 화면이 큰것이 이점이 있다.\\n\\n5. Dvd part (cd Rom)\\n3번이 읽기 쓰기 속도가 가장 빠름 -> \\n\\n\\n\\n\\n나머지 부분들\\n첫번째 : 블루투스가 된다\\n두번째 : 무선 랜이 된다 (와이파이) , 디지털 카메라\\n3번째는 7.1 채널 스피커가 지원된다\\n\\n6. Audio part\\n\\n\\n7. Network part\\n\\n8. Os part\\n\\n9. Graphic card part\\n3번만 외장이 있음\\n"}'.encode()
    #response = requests.post('https://api.gptzero.me/v2/predict/text', cookies=cookies, headers=headers, data=data)