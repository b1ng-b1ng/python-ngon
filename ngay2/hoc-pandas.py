import pandas as pd
# print(pd.__version__)
# s = [1,2,3,"la"]
# sp = pd.Series(s,index=["a","b","c","d"])
# sp.loc["a"] = 200
# print(sp.loc["a"])
# # doc gia tri ở dòng có ký tự nào thì dùng loc["ký tự"]
# # đọc giá trị nhưng ở thứ tự thì dùng iloc
# print(sp.iloc[1])
# print(sp.iloc[3])
# print(sp)
# calo = {'Day 1': 1202,"Day 2":2121,"Day 3":1202}
# calo = pd.Series(calo)
# calo.loc["Day 2"] = 1222
# calo.iloc[1] += 1000
# print(calo)
# print(calo[calo < 2000])
data = [100,200,300]
data = pd.Series(data)
print(data[data > 200])
