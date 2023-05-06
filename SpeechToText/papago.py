from dotenv import load_dotenv
import os

load_dotenv()

import sys
import urllib.request
#-*- coding: utf-8 -*-
import json
client_id = os.environ.get('PAPAGO_client_id') # 개발자센터에서 발급받은 Client ID 값
client_secret = os.environ.get('PAPAGO_client_secret') # 개발자센터에서 발급받은 Client Secret 값

korText = "성 소수자인 삼촌에게 노래를 헌정했던 미국 팝스타 비욘세가 동성애를 금지한 아랍에미리트(UAE) 두바이에서 300억 원에 육박하는 출연료를 받고 호화 공연을 펼쳐 성 소수자들로부터 비판을 받고 있다. 성 소수자인 삼촌에게 노래를 헌정했던 미국 팝스타 비욘세가 동성애를 금지한 아랍에미리트(UAE) 두바이에서 300억 원에 육박하는 출연료를 받고 호화 공연을 펼쳐 성 소수자들로부터 비판을 받고 있다. "
encText = urllib.parse.quote(korText)

data = "source=ko&target=en&text=" + encText
url = "https://openapi.naver.com/v1/papago/n2mt"
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request, data=data.encode("utf-8"))
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    #print(response_body.decode('utf-8'))
    result = json.loads(response_body.decode('utf-8'))
    print(result['message']['result']['translatedText'])
else:
    print("Error Code:" + rescode)