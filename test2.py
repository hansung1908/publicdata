import requests, xmltodict, json
import openpyxl
import pandas as pd

api_key = "서비스키"
url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst?serviceKey={}&numOfRows=10&pageNo=1&base_date=20231007&base_time=0600&nx=55&ny=127'.format(api_key)

content = requests.get(url).content
dict = xmltodict.parse(content)

# 딕셔너리를 JSON 파일로 저장
with open('data.json', 'w', encoding='utf-8') as json_file:
    json.dump(dict['response']['body']['items']['item'], json_file, ensure_ascii=False, indent=4)

# JSON 파일을 읽어서 데이터프레임으로 변환
with open('data.json', 'r', encoding='utf-8') as json_file:
    data = pd.read_json(json_file)

# JSON 데이터를 데이터프레임으로 변환
df = pd.DataFrame(data)

# 데이터프레임을 엑셀 파일로 저장
df.to_excel('공공데이터.xlsx', index=False, engine='openpyxl')

print(df)