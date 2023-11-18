# publicdata
- 날씨 앱이나 미세먼지 앱을 만들기 위해선 데이터가 필요
- 데이터 구성을 위해 직접 웹 스크래핑을 통해 긁어오는 것도 하나의 방법이지만 시간도 오래 걸리고 품질또한 보장을 못하며 저작권과 관련한 문제가 생길 가능성 o
- 공공 데이터 포털은 다양한 분야의 양과 품질이 포장된 데이터를 국가에서 무료로 제공
- 공공데이터 api 사용시 사용신청을 하고 승인을 받은 뒤에 보안키와 함께 사용을 승인한다. 승인기간은 보통 1시간정도

### 국토교통부_아파트매매 실거래 상세 자료
- 부동산 거래 정보 api를 보다 쉽게 다루기 위해 PublicDataReader 모듈을 다운받아 활용
- 공공데이터를 받아 결과를 보기 위해선 주피터 환경을 설치하여 각각 셀로 분할 후 결과 확인이 가능

### 기상청_단기예보 + 시간, 일자료 조회서비스
- 단기예보 데이터는 초단기예보시 1일 이내, 단기예보시 3일 이내의 데이터만 사용 가능
- 기상청 지상 일자료 데이터는 당일로부터 전날까지 데이터만 사용가능
