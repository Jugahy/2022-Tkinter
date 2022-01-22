"""
1. filtering

    1-1. small = df[df["입학정원 합(명)"]<3000]
    1-2. medium = df[(3000<=df["입학정원 합(명)"]) & (df["입학정원 합(명)"]<8000)]
    1-3. large = df[8000<=df["입학정원 합(명)"]]


2. 열 선택, 추가

    2-1. df["Small"] = small["입학정원 합(명)"]
    2-2. df["Medium"] = medium["입학정원 합(명)"]
    2-2. df["Large"] = large["입학정원 합(명)"]


3. 누락 데이터 처리

    3-1. df['Small'].value_counts(dropna=False), df['Medium'].value_counts(dropna=False), df['Large'].value_counts(dropna=False)

    3-2. 문제)Small, Medium, Large 누락 데이터들 어디의 값인지 알려주기

        3-2-1. for i in range(df.shape[0]):
                    if df["Small"][i] == "not_S":
                        if df["Medium"][i] == "not_M":
                            df.loc[i,"Small"] = "L"
                        else:
                            df.loc[i,"Small"] = "M"
                    else:
                        pass

        3-2-2. for i in range(df.shape[0]):
                    if df["Medium"][i] == "not_M":
                        if df["Small"][i] == "not_S":
                            df.loc[i,"Medium"] = "S"
                        else:
                            df.loc[i,"Medium"] = "L"
                    else:
                        pass

        3-2-3. for i in range(df.shape[0]):
                    if df["Large"][i] == "not_L":
                        if df["Large"][i] == "not_L":
                            df.loc[i,"Large"] = "M"
                        else:
                            df.loc[i,"Large"] = "S"
                    else:
                        pass

4. 원하는 정보를 갖는 dataframe 만들기

    4-1. df.drop(["Medium","Large"],axis=1)
    4-2. df.drop(["Small","Large"],axis=1)
    4-3. df.drop(["Small","Medium"],axis=1)


"""

"""
1. 각 식당ID 에 속하는 음식들의 가격 평균을 출력하세요
2. 각 식당ID 에 속하는 음식들의 개수의 평균을 출력하세요

# print(df[df["식당명"].str.find("전주대점") >= 0])
# print(df[df["식당명"].str.endswith("전주대점")])
"""