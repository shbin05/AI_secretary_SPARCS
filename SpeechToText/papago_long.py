#-*- coding: utf-8 -*-
from dotenv import load_dotenv
import os

load_dotenv()
import requests

client_id = os.environ.get('PAPAGO_client_id') # chatGPT API KEY
client_secret = os.environ.get('PAPAGO_client_secret') # 개발자센터에서 발급받은 Client Secret 값
url = "https://openapi.naver.com/v1/papago/n2mt"

def translate(option, data) :   
    #data = "성 소수자인 삼촌에게 노래를 헌정했던 미국 팝스타 비욘세가 동성애를 금지한 아랍에미리트(UAE) 두바이에서 300억 원에 육박하는 출연료를 받고 호화 공연을 펼쳐 성 소수자들로부터 비판을 받고 있다. 성 소수자인 삼촌에게 노래를 헌정했던 미국 팝스타 비욘세가 동성애를 금지한 아랍에미리트(UAE) 두바이에서 300억 원에 육박하는 출연료를 받고 호화 공연을 펼쳐 성 소수자들로부터 비판을 받고 있다. "
    #요청 파라미터
    if option == "krTOen" :
        req_param = {"source":"ko", "target":"en", "text":data}
    else :
        req_param = {"source":"en", "target":"ko", "text":data}

    #요청 헤더
    req_header = {"X-Naver-Client-Id":client_id, "X-Naver-Client-Secret":client_secret}
    #print(req_param)

    res = requests.post(url,headers=req_header, data=req_param)

    #print(res.status_code, res.ok)
    if res.ok:
        trans_txt=res.json()['message']['result']['translatedText']
        return trans_txt
    else:
        print('error code', res.status_code)

text = "강남 크루팩토리 승무원학원은 카타르 항공 승무원 오픈데이를 시작으로 3월에만 10명이상의 외항사 승무원이 최종합격을 한데 이어 19년 상반기 아시아나항공 및 대한항공 승무원채용에서도 다수의 합격자를 배출 하였다. 국내항공사 면접과 외국항공사 면접방식은 차이가 있다. 그렇기에 항공사별 면접 방식에 맞춰 수강생들을 준비시키며, 전문성을 높인 것이 다수 합격자를 배출한 결과로 이어졌다. 보통 외국항공사 면접은 cover letter, resume등의 이력서 작성부터 그룹디스커션, 스몰톡 영어필기테스트, 사진묘사등 항공사 마다 면접 방식이 조금씩은 상이하지만 국내항공사 면접은 서류통과자에 한해 실무, 임원, 최종(대한항공)면접과 체력테스트, 수영테스트가 진행이 된다. 크루팩토리 승무원학원 대표이사는 승무원이라는 직업의 역할은 동일하겠지만 각 나라별, 항공사별 그들의 조직체계와, 문화, 인종 등 여러 상황을 고려해 항공사에서 평가하는 면접기준이 분명 하게 나뉘어져 있어 최종합격을 위해서는 소그룹으로 운영하여 원하는 항공사 면접 과정을 선택해서 경쟁력을 키우는 것이 최종 합격을 하는 중요한 요소라고 전했다. 국내에서 소수정예 승무원학원으로 시작한 크루팩토리는 인원제한을 8명기준으로 실제 면접시 한조의 인원수와 비슷하게 비율을 맞춰 첫지원자와 재지원자 그리고 국내항공사 희망자와 외항사 희망자를 구분하여 승무원과외식 트레이닝을 하고 있다. 각 과목별로 항공사 면접관 출신과 아나운서 교관, 헤어, 메이크업 전문강사, 국내, 외항사 경력 약 10년 안팎의 경력을 갖춘 유명 강사, 교수들로 구성되어 있고 원장과 부원장이 교수실에서 전체적인 수업과 학생들 이력서 관리부터 최종합격시까지 철저한 관리를 책임지고 있다. 크루팩토리는 대한항공과 아시아나항공 승무원 최종합격생을 초빙하여 합격생 간담회를 실시할 예정이다. 최종합격생들의 스펙과 면접분위기 와 준비방법 그리고 합격의 원동력이 무엇인지 등에 대해 오픈할 예정이다. 크루팩토리 취업 팀장은 상반기 채용이 마무리 되었지만, 얼마 지나지 않아 중반기 채용이 바로 공지될 예정이라며, 상반기 탈락의 고배를 마신 승무원 지원자들은 이번 경험을 토대로 철저한 준비를 통해 중반기 채용의 기회를 꼭 놓치지 않기를 바란다고 전했다. 중반기 항공사 준비문의 및 승무학원 수강료(가격)문의는 크루팩토리 승무원학원(서울강남점, 인천점)사이트를 통해 확인 할 수 있다."
print(translate("krTOen",text))