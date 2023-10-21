# request : 날씨 데이터를 url을 통해 가져오기 위해 사용
import requests
# xmltodict : xml 데이터를 딕셔너리로 바꿔주기 위해 사용
import xmltodict
# datetime : 현재 시간
import datetime
# certifi : url 접속시 ssl 인증 오류 방지를 위해 사용
import certifi
# tkinter : 파이썬 gui 프로그램
import tkinter as tk
from tkinter import Label

# 현재 시간을 가져와 저장
tmp = datetime.datetime.now()
# url에 삽입하기 위해 형태 변경
now_date, now_time = str(tmp).replace("-", "").split() # ex) 20231022
now_time = (now_time[0:2]) + "00" # ex) 0600

# 서울, 부산, 대구, 인천, 광주, 대전, 울산, 세종, 경기도, 충북, 충남, 전북, 전남, 경북, 경남, 제주순으로 좌표값
xy_list = [(60, 127), (98, 76), (89, 90), (55, 124), (58, 74), (67, 100), (102, 84), (66, 103),\
           (60, 120), (69, 107), (68, 100), (63, 89), (51, 67), (89, 91), (91, 77), (52, 38), (73, 134)]

# 공공데이터 포털에서 단기예보api를 사용하기 위한 api키
api_key = "1%2FCFOLYKPhbqr5KCMfu2IA4Zl25N6B7KedYBRbxuh3AbeigZpcJtFG3pdO9DUDgohN8Qe2L%2BdHjidB1dwABAaQ%3D%3D"

# 각 지역 이름
locations = ["서울", "부산", "대구", "인천", "광주", "대전", "울산", "세종", "경기", "충북", "충남", "전북", "전남", "경북", "경남", "제주"]

# 각 지역의 온도, 강수량, 풍속
temperature = []
precipitation = []
wind_speed = []

# 지역 수 만큼 각 좌표에 해당하는 온도, 강수량, 풍속 정보를 각 리스트에 담아줌
for i in range(0, len(xy_list)):
    # 해당 url에 api키, 시간대, 좌표 정보를 넣어줘 데이터를 띄움
    url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst?serviceKey={}&numOfRows=10&pageNo=1&base_date={}&base_time={}&nx={}&ny={}'\
    .format(api_key, now_date, now_time, xy_list[i][0], xy_list[i][1])
    
    # 해당 url에 띄워진 데이터를 크롤링해서 가져옴
    # 이때 ssl 인증서 오류가 발생할 수 있으므로 verify=certifi.where() 옵션을 통해 인증서를 찾아서 직접 인증
    content = requests.get(url, verify=certifi.where()).content
    # 가져온 데이터를 딕셔너리 형태로 변경
    dict = xmltodict.parse(content)

    # 각 데이터에서 필요한 부분만 가져와 각 리스트에 추가
    temperature.append(dict['response']['body']['items']['item'][3]['obsrValue']) # 기온
    precipitation.append(dict['response']['body']['items']['item'][2]['obsrValue']) # 강수량
    wind_speed.append(dict['response']['body']['items']['item'][7]['obsrValue']) # 풍속

# 지역 데이터와 날씨 데이터를 딕셔너리로 정리
weather_data = {}
for i in range(len(locations)):
    weather_data[locations[i]] = {
        "기온": temperature[i],
        "강수량": precipitation[i],
        "풍속": wind_speed[i]
    }

# gui 생성시 입력받은 지역에 날씨를 띄워주는 함수
def get_weather():
    # gui에서 입력받은 값을 받아와 저장
    city = city_entry.get()
    # 해당 지역과 매칭되는 날씨 정보 가져와 저장
    weather_info = weather_data.get(city, "날씨 정보를 찾을 수 없습니다.")
    # gui에 해당 지역과 날씨 정보 출력
    result_label.config(text=f"지역: {city}\n기온: {weather_info['기온']}℃\n강수량: {weather_info['강수량']}mm\n풍속: {weather_info['풍속']}m/s")

# gui 프로그램 생성
app = tk.Tk()
app.title("날씨 앱") # 띄운 창 제목
app.geometry("400x300") # 띄운 창의 크기

# 지역 이름을 입력하라는 안내
city_label = tk.Label(app, text="지역 선택:")
city_label.pack()

# 지역 이름 입력
city_entry = tk.Entry(app)
city_entry.pack()

# 해당 버튼 클릭시 get_weather 함수를 불러와 입력했던 지역 이름을 바탕으로 날씨 정보 가져옴
get_weather_button = tk.Button(app, text="날씨 가져오기", command=get_weather)
get_weather_button.pack()

# 가져온 날씨 정보를 출력
result_label = tk.Label(app, text="", font=("Helvetica", 14))
result_label.pack()

# 다 설정한 gui 창을 실행하여 띄움
app.mainloop()