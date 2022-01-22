import pandas as pd

df = pd.read_csv("univ.csv", encoding='euc_kr')
# print(df.shape[0])
# for i in range(df.shape[0]):
#     if df["대학명"][i] in "기술":
#         print(df["대학명"][i])
#     else:
#         pass

for i in range(df.shape[0]):
    if len(df["대학명"][i]) == 5:
        print(df["대학명"][i])
    else:
        pass


# print(df.loc[df["대학명"].str.find("기술")>=0])
# print(df.loc[df["대학명"].str.rfind("기술")>=0])

# print(df.loc[df["대학명"].str.endswith("원")])
# small = df[df["입학정원 합(명)"]<3000]
# medium = df[(3000<=df["입학정원 합(명)"]) & (df["입학정원 합(명)"]<8000)]
# large = df[8000<=df["입학정원 합(명)"]]
#
# df["Small"] = small["입학정원 합(명)"]
# df["Medium"] = medium["입학정원 합(명)"]
# df["Large"] = large["입학정원 합(명)"]
#
# print(df['Small'].value_counts(dropna=False))
# print(df['Medium'].value_counts(dropna=False))
# print(df['Large'].value_counts(dropna=False))
#
# df["Small"].fillna("not_S", inplace=True)
# df["Medium"].fillna("not_M", inplace=True)
# df["Large"].fillna("not_L", inplace=True)
#
#
# for i in range(df.shape[0]):
#     if df["Small"][i] == "not_S":
#         if df["Medium"][i] == "not_M":
#             df.loc[i,"Small"] = "L"
#         else:
#             df.loc[i,"Small"] = "M"
#     else:
#         pass
#
# for i in range(df.shape[0]):
#     if df["Medium"][i] == "not_M":
#         if df["Small"][i] == "not_S":
#             df.loc[i,"Medium"] = "S"
#         else:
#             df.loc[i,"Medium"] = "L"
#     else:
#         pass
#
# for i in range(df.shape[0]):
#     if df["Large"][i] == "not_L":
#         if df["Large"][i] == "not_L":
#             df.loc[i,"Large"] = "M"
#         else:
#             df.loc[i,"Large"] = "S"
#     else:
#         pass
#
# print(df.drop(["Medium","Large"],axis=1))
#
#
#
#
#
# # # df.loc[0,"Small"] = "a"
# # print(df["Small"])
# # print(df)
#
# # print(df["Small"][0])
#
# # print(df)
#
#


