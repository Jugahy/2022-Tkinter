"""
USE DATA : https://www.kaggle.com/c/titanic/data

import pandas as pd

pd.set_option('display.max_columns', None)

# 1. titanic.csv 파일 읽어오기
df = pd.read_csv("titanic.csv")


# 2. 생존자 수/사망자 수 출력
2-1.
    df[df["survived"] == 1]["survived"].count() # 생존자
    df[df["survived"] == 0]["survived"].count() # 사망자
2-2.
    df["survived"].value_counts()


# 3. 탑승권 등급별(1,2,3등실) 인원 출력
3-1.
    df[df["pclass"] == 1]["pclass"].count()
    df[df["pclass"] == 2]["pclass"].count()
    df[df["pclass"] == 3]["pclass"].count()
3-2.
    df["pclass"].value_counts()


# 4. 탑승자 중 탑승항구가 표시되지 않은 명단 출력
df[df["embarked"].isnull()]


# 5. 탑승권 등급별(1,2,3등실) 요금의 평균 출력
df.groupby("pclass")["fare"].mean()


# 6. 나이(age)의 NaN값을 age의 평균으로 채우기
df["age"].fillna(df["age"].mean(),inplace=True)


# 7. 생존자의 이름, 나이, 탑승권 등급 출력
ddf = df[df["pclass"] == 1]
ddf[["name","age","pclass"]]


# 8. 생존자 중 나이가 30 미만 명단 출력
df[(df["survived"] == 1) & (df["age"] < 30)]


# 9. 탑승자 중 여성 명단 출력
df[df["sex"] == "female"]


# 10. 탑승자 중 Miss 명단 출력
10-1.
    df[df["name"].str.find("Miss") >= 0]
10-2. 대소문자 구분하지 않음
    df[df["name"].str.contains("Miss",case=False)]



# 11. 각 pclass 요금의 최소값들을 구하되 0이 아닌 것
df[df["fare"]>0].groupby("pclass")["fare"].min()


# 12. 정보 보기
df.info()

"""




