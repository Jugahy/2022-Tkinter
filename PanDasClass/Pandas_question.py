"""
문제
    입학정원을 기준으로 학교의 크기를 예측해보기 위해 입학정원에 특정 기준으로 학교의 크기를 small, medium, large
    로 나누어 크기에 따른 3개의 DataFrame 만들기위해 학교의 입학정원 별로 학교의 크기는
    3000 미만은 small, 3000이상 8000미만 medium, 8000이상은 large


1. filtering

    1-1. small 변수에 입학정원 합(명)이 3000 미만인 학교를 넣어주세요.
    1-2. medium 변수에 입학정원 합(명)이 3000이상 8000미만인 학교를 넣어주세요.
    1-3. large 변수에 입학정원 합(명)이 8000이상인 학교를 넣어주세요.


2. 열 선택, 추가

    2-1. small 변수에 입학정원 합(명)의 정보만 df에 Small 변수로 열 추가
    2-2. medium 변수에 입학정원 합(명)의 정보만 df에 Medium 변수로 열 추가
    2-2. large 변수에 입학정원 합(명)의 정보만 df에 Large 변수로 열 추가


3. 누락 데이터 처리, 원소 다루기

    3-1. small,medium,large 누락 데이터들의 개수들을 각각 출력
    3-2. Small, Medium, Large 누락 데이터들 어디의 값인지 알려주기
        3-2-1. Small 누락 데이터를 (M 또는 L) 치환
        3-2-2. Medium 누락 데이터를 (S 또는 L) 치환
        3-2-3. Large 누락 데이터를 (S 또는 M) 치환

4. 원하는 정보를 갖는 dataframe 만들기

    4-1. 기존 df에 Small 열만 추가
    4-2. 기존 df에 Medium 열만 추가
    4-3. 기존 df에 Large 열만 추가

"""
"""
import pandas as pd


# 데이터 가져오기
df = pd.read_csv("univ.csv", encoding='euc_kr')


# 데이터 정보 보기
df.describe()
df.info


# 그룹 연산 groupby
dff = df.groupby(["지역별"])
dff.count()


# filter
df[df["지역별"]=="전북"]
df[(df["지역별"]=="전북") & (df["설립별"]=="사립")]

# 전체 행,열 보기
pd.set_option("display.max_(rows,columns)",None)

"""


"""

언어 선택
내가 원하는 식당의 이름을 검색하면 그 식당의 메뉴들을 볼 수 있으면 좋지 않을까?
가격도 같이 볼 수 있게?

"""

