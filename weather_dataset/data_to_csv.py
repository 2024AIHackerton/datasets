import csv
import requests
import chardet

tm1 = "20240101"    # 시작일
tm2 = "20241025"    # 종료일
stn = "0"           # 전체지점 => 0
help = "0"          # 필드 도움말 없으면 0
authKey = "dD7wQQpvQFa-8EEKbzBWRQ"        # 인증키

# URL 문자열
url = f'https://apihub.kma.go.kr/api/typ01/url/kma_sfcdd3.php?tm1={tm1}&tm2={tm2}&stn={stn}&help={help}&authKey={authKey}'
# GET 요청
response = requests.get(url)

# 응답의 Content-Type 확인
content_type = response.headers.get('Content-Type')
print("Content-Type:", content_type)

# 인코딩 감지 및 디코딩
encoding = chardet.detect(response.content)['encoding']  # 인코딩 감지
decoded_content = response.content.decode(encoding or 'EUC-KR')  # 인코딩으로 디코딩
print("응답 내용:", decoded_content)  # 응답 내용을 확인하여 형식 파악

# 헤더 설정
header = [
    "TM", "STN", "WD", "WS", "GST_WD", "GST_WS", "GST_TM", "PA", "PS", "PT",
    "PR", "TA", "TD", "HM", "PV", "RN", "RN_DAY", "RN_JUN", "RN_INT", "SD_HR3",
    "SD_DAY", "SD_TOT", "WC", "WP", "WW", "CA_TOT", "CA_MID", "CH_MIN", "CT",
    "CT_TOP", "CT_MID", "CT_LOW", "VS", "SS", "SI", "ST_GD", "TS", "TE_005",
    "TE_01", "TE_02", "TE_03", "ST_SEA", "WH", "BF", "IR", "IX"
]

# 데이터를 줄 단위로 나누기
lines = decoded_content.strip().split("\n")

# 필요한 데이터 추출
# 데이터 6시간 단위로 추출함
is_reading = False
filtered_data = []
line_counter = 0
for line in lines:
    if line.startswith("#START7777"):
        is_reading = True
        continue
    elif line.startswith("#END7777"):
        is_reading = False
        continue
    elif line.startswith("#") or not is_reading:
        continue

    # 12번째 줄마다 데이터를 추가
    line_counter += 1
    if line_counter % 12 == 0:
        filtered_data.append(line.split())

# CSV 파일로 저장
csv_file = f"weather_data_{tm1}_{tm2}.csv"
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(header)  # 헤더 작성
    writer.writerows(filtered_data)   # 데이터 작성

print(f"데이터가 '{csv_file}' 파일에 성공적으로 저장되었습니다.")
