import pandas as pd
datas = [[65,92,78,83,70], [90,72,76,93,56], [81,85,91,89,77], [79,53,47,94,80]]
indexs = ["林大明", "陳聰明", "黃美麗", "熊小娟"]
columns = ["國文", "數學", "英文", "自然", "社會"]
df = pd.DataFrame(datas, columns=columns,  index=indexs)
print('df.loc["陳聰明"]["數學"] (原始)：' + str(df.loc["陳聰明"]["數學"]))
df.loc["陳聰明"]["數學"] = 91
print('df.loc["陳聰明"]["數學"] (修改)：' + str(df.loc["陳聰明"]["數學"]))
print()
print('df.loc["陳聰明", :] ->')
df.loc["陳聰明", :] = 80
print(df.loc["陳聰明", :])
