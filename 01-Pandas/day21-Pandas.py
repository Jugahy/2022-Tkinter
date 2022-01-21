import pandas as pd
import numpy as np
import numpy.ma as ma

# 2848
"""
# univ 파일 읽어와 df에 저장
df = pd.read_csv("univ.csv", encoding='euc_kr')

# 위 df 파일에서 평균입학금(원) 열 삭제
df.drop("평균입학금(원)", axis=1, inplace=True)

# 위 df 파일에서 2,3 행 삭제
df.drop([2,3], axis=0, inplace=True)

# df 1번 행 선택
df.iloc[1]

# df에서 대학명 열 선택
df["대학명"]

# 0,1 행과 대학명, 지역별 열 선택 후 df2에 저장
df2 = df.loc[[0,1], "대학명":"지역별"]

# df2 시 열 추가 하기 "강릉시", "강원시"
df2["시"] = ["강릉시","강원시"]

# df2(예시) 행 추가하기
df2.loc[2] = ["강강대학교","강원","강시"]

# df2 대학명 열을 인덱스로 배정
df2.set_index("대학명",inplace=True)

# df2 원소값 변경 (강원대학교 강원도를 전주시로 변경)
df2.loc["강원대학교","시"] = "전주시"

# df2 행 열의 위치를 바꾸시오
df2.T

# 지역별이 전북인 데이터 추출
df[df["지역별"] == "전북"]
"""

# 9437
"""
# data.go.kr 에서 한국장학재단_대학별 평균등록금 csv파일을 다운받은 후 출력하세요
df = pd.read_csv("univ.csv",encoding="euc_kr")

# 전국의 국공립대학의 개수는? (국공립의 갯수와 데이터프레임의 index를 0부터 순차적으로 나오게 출력해주세요)
len(df[df["설립별"] == "국공립"])

# 전문대학중 평균등록금(원) 이 가장 비싼 대학은?
df[df["학제별"] == "전문대학"]["평균등록금(원)"].max()  # 최대 평균등록금(원)
df[df["평균등록금(원)"] == df[df["학제별"] == "전문대학"]["평균등록금(원)"].max()]  # 행

# 사립 대학중 평균입학금이 0이 아닌 최저값 대학은?
df[df["설립별"] == "사립"]["평균등록금(원)"].min()  # 최소 평균등록금(원)
df[df["평균등록금(원)"] == np.min(ma.masked_where(df[df["설립별"] == "사립"]["평균등록금(원)"]==0,df[df["설립별"] == "사립"]["평균등록금(원)"]))]  # 행

# 국공립대학중 입학정원 합(명)이 두번째로 높은 대학은?
aa = df[df["설립별"] == "국공립"]["입학정원 합(명)"]  # 두 번째로 높은 대학
df[df["입학정원 합(명)"] == sorted(aa, reverse=True)[1]]  # 행

# 국공립대학중 입학정원 합(명)이 10000 이상인 대학들을 모두 출력하세요
df[df["입학정원 합(명)"]>=10000]

# 입학정원 합(명)이 10000 이상인 사립대학을 모두 출력하세요
df[(df["입학정원 합(명)"]>=10000) & (df["설립별"]=="사립")]

# [지역별]을 포함하는 대학명을 모두 출력하세요

# country = df["지역별"].drop_duplicates(inplace=False)
# country = country.reset_index()
# country = country.drop("index",axis=1)
#
# for i in range(df.shape[0]):
#     for j in range(17):
#         if country.loc[j,"지역별"] in df["대학명"][i]:
#             print(df["대학명"][i])
#             break
#         else:
#             pass

# 다운받은 한국장학재단_대학별 평균등록금 csv파일에 (387행 대학 국공립 강진대학교 전남 20000 0 3200000) 행을 추가한 후 출력하세요

# lisst = {"학제별":"대학", "설립별":"국공립", "대학명":"강진대학교", "지역별":"전남","입학정원 합(명)":20000, "평균입학금(원)":0, "평균등록금(원)":3200000}
# df1 = df.append(lisst, ignore_index=True)
# print(df1)

# 다운받은 한국장학재단_대학별 평균등록금 csv파일의 4행을 삭제한 후 출력하세요
# df.drop([4],axis=0,inplace=True)
# print(df)

# 다운받은 한국장학재단_대학별 평균등록금 csv파일에서 1행의 평균등록금을 평균등록금 전체의 평균으로 바꾼 후 정수로 출력하세요
# df.loc[1,"평균등록금(원)"] = df["평균등록금(원)"].mean()
# print(df)

# 사립대학중 입학정원 합(명)이 10000 이상이며 평균등록금이 4000000 이하인 학교를 모두 출력하세요

# a = df[df["설립별"] == "사립"]
# b = a[a["입학정원 합(명)"]>=10000]
# print(b[b["평균등록금(원)"]<=4000000])
# df

# 다운받은 한국장학재단_대학별 평균등록금 csv파일의 행과 열을 바꾼 후 출력하세요
# print(df.T)

"""
"""# .drop_duplicates()
df = pd.read_csv("eat.csv")
# pd.set_option('display.max_rows', None)



b = df.sort_values(by="식당ID")
# df.drop(["메뉴ID","메뉴태그정보","메뉴명-로마자","메뉴태그-영어","메뉴태그-일본어","메뉴태그-중국어(간체)"],axis=1,inplace=True)
b = b.drop_duplicates(["식당ID"])

# df.drop_duplicates(["식당ID"],inplace=True)
df["메뉴개수"] = df.groupby("식당ID")["메뉴명"].count()
df["메뉴평균"] = df.groupby("식당ID")["메뉴가격"].mean()




# df.groupby("식당ID")["메뉴가격"].mean()
# df.drop_duplicates(["식당ID"],inplace=True)
#
# df.reset_index(inplace=True)
# df.drop("index",axis=1,inplace=True)
# print(df.groupby("식당ID")["메뉴가격"].mean())
# print(df.groupby("식당ID")["메뉴명"].count())


# print(df.groupby("식당ID")["메뉴가격"].mean().drop(["식당ID"],axis=1))
print(df["메뉴개수"].drop(["식당ID"],axis=1))
# print(df.groupby("식당ID")["메뉴명"].count())
# print(df.sort_values(by="식당ID"))
# b["메뉴개수"] = df.groupby("식당ID")["메뉴명"].count()
# b["메뉴평균"] = df.groupby("식당ID")["메뉴가격"].mean()

# b.drop(["메뉴ID","메뉴태그정보","메뉴명-로마자","메뉴태그-영어","메뉴태그-일본어","메뉴태그-중국어(간체)"],axis=1,inplace=True)
# print(b)"""
"""pd.set_option('display.max_columns', None)
df = pd.read_csv("eat.csv")
# print(df["메뉴가격"].max())

# a = df.sort_values(by="메뉴가격")
# print(a.tail(5))


# print(df[df["식당명"].str.find("전주대점") >= 0])
# print(df[df["식당명"].str.endswith("전주대점")])


# df[df["평균등록금(원)"] == np.min(ma.masked_where(df[df["설립별"] == "사립"]["평균등록금(원)"]==0,df[df["설립별"] == "사립"]["평균등록금(원)"]))]

# print(df.groupby("메뉴명").mean())

# a = df[df["식당명"].str.contains("파리바게뜨 전주대점")]
# print(a[a["메뉴명"].str.contains("아메리카노")])


# print(df["메뉴명"].isnull())

# df.dropna(axis=0, thresh=1, inplace=True)
# print(df)

# print(df.fillna("x"))

# df["메뉴태그-영어"].fillna("None",inplace=True)
# a = df[(df["식당명"] == "청년다방") & (df["메뉴명"] == "불향차돌세트(중)")]
# print(a)

# a = df[df["식당명"] == "청년다방"]
# print(a[a["메뉴명"] == "불향차돌세트(중)"])
# a = df[df["설립별"] == "사립"]
# b = a[a["입학정원 합(명)"]>=10000]
# print(b[b["평균등록금(원)"]<=4000000])
# df
# print(df.groupby(["식당명"]))"""


# 2494
"""
df = pd.read_csv("eat.csv")
pd.set_option('display.max_columns', None)

# 1. 가격이 제일 비싼 5개 메뉴 추출
df.sort_values(by="메뉴가격").tail(5)

# 2. ‘식당ID’ 864184 의 메뉴 추출
df[df["식당ID"] == 864184]

# 3. 식당 별 메뉴 개수 추출
df.groupby("식당명")["메뉴명"].count()

# 4. ‘식당명’ 을 기준으로 ‘메뉴가격’ 의 평균,최대,최소 한번에 추출
a = df.groupby(["식당명"]).agg(["min","max"])
a["메뉴가격"]

# 5. ‘순대국밥’ 이 포함된 메뉴 추출
b = df[df["메뉴명"].str.find("순대국밥") >= 0]

# 6. ‘순대국밥’ 이 포함된 메뉴들의 평균 가격
b["메뉴가격"].mean()

# 7. ‘껌’ 으로 시작하는 메뉴 추출
df[df["메뉴명"].str.find("껌") == 0]

# 8. ‘메뉴명’ 이 35글자인 메뉴 추출
df[df["메뉴명"].str.len() >= 35]

# 9. ‘메뉴가격’ 이 10000원 인 메뉴 추출
df[df["메뉴가격"] == 10000]

# 10. df의 NaN 값 ‘이연승’ 으로 채우기
df.fillna("이연승")
"""

df = pd.read_csv("../PanDasClass/eat.csv")
#print(df.groupby("식당명")["메뉴명"])

# grp = df.groupby("식당명")
#
# # print(grp.head(1)["메뉴명"])
#
# for idx, g in grp:
#     print(g.head(1))
