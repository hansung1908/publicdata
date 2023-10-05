import json
import urllib.request

key = "서비스 키 입력"

url = "http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst?serviceKey=" + key + "&dataType=JSON&areaNo=1100000000&time=2021111818"
json_page = urllib.request.urlopen(url)
json_data = json_page.read().decode("utf-8")
json_array = json.loads(json_data)

print(json_array)