import requests

api_key = "서비스키"
url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst?serviceKey={}&numOfRows=10&pageNo=1&base_date=20231006&base_time=0600&nx=55&ny=127'.format(api_key)

response = requests.get(url)
print(response.content)