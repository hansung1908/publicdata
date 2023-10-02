# 1. 라이브러리 임포트하기
from PublicDataReader import TransactionPrice
import PublicDataReader as pdr

# 2. 공공 데이터 포털 OpenAPI 서비스 인증키 입력하기
service_key = "공공데이터포털에서 발급받은 인코딩 서비스 키"

# 3. 국도교통부 실거래가 정보 조회 OpenAPI 세션 정의하기
# debug : True이면 모든 메세지 출력, False이면 오류 메세지만 출력 (기본값 : False)
api = TransactionPrice(service_key)

# 4. 지역코드(시군구코드) 검색하기
sigungu_name = "분당구" # 시군구코드 : 41135
code = pdr.code_bdong()
code.loc[(code['시군구명'].str.contains(sigungu_name)) &
         (code['읍면동명']=='')]

# 5. 특정 년월 자료만 조회하기
df = api.get_data(
    property_type="아파트", # 부동산 상품 종류(아파트, 오피스텔, 단독다가구 등)
    trade_type="매매", # 부동산 거래 유형(매매, 전월세)
    sigungu_code="41135",
    year_month="202212",
    )

df.tail()

# 6. 특정 기간 자료 조회하기
df = api.get_data(
    property_type="아파트", # 부동산 상품 종류(아파트, 오피스텔, 단독다가구 등)
    trade_type="매매", # 부동산 거래 유형(매매, 전월세)
    sigungu_code="41135",
    start_year_month="202212",
    end_year_month="202301",
    )
    
df.tail()