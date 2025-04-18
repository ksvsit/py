import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  #繪圖中文字型
plt.rcParams["axes.unicode_minus"] = False 
datas = [[65,92,78,83,70], [90,72,76,93,56], [81,85,91,89,77], [79,53,47,94,80]]
columns = ["國文", "數學", "英文", "自然", "社會"]
df = pd.DataFrame(datas, columns=columns)
df.plot(xticks=range(0,4))
