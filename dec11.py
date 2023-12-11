import FinanceDataReader as fdr
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

""" x1 = [2,3,6,7,10]
x2 = [1,4,5,8,9]

y1 = [1,4,5,8,9]
y2 = [2,4,6,8,10]


#plt.subplot(2, 1, 1)    
#plt.subplot(1, 2, 1)
#plt.subplot(3, 1, 1)
#plt.subplot(2, 2, 1)
plt.plot(x1, y1, "o-")

plt.title("X1 Graph")
plt.xlabel("x-data")
plt.ylabel("y-data")

plt.style.use("bmh")


#plt.subplot(2, 1, 2)
#plt.subplot(1, 2, 2)
#plt.subplot(3, 1, 2)
#plt.subplot(2, 2, 2)
plt.plot(x2, y2, ".-")

plt.title("X2 Graph")
plt.xlabel("x2-data")
plt.ylabel("y2-data")


#plt.subplot(3, 1, 2)
#plt.subplot(2, 2, 3)
plt.plot(x1, x2, ".-")
plt.plot(x2, x1, ".-")

plt.title("X3 Graph")
plt.xlabel("x3-data")
plt.ylabel("y3-data")

plt.style.use("classic")

#plt.subplot(2, 2, 4)
plt.plot(x1, x2, ".-")
plt.plot(x2, x1, ".-")

plt.title("X4 Graph")
plt.xlabel("x4-data")
plt.ylabel("y4-data")

plt.style.use("Solarize_Light2")
plt.tight_layout()

plt.savefig("data/img.jpg")
plt.savefig("data/img.png")


plt.show() """


# 다중 막대그래프 그리기 

""" x_years = ["2020", "2021", "2022"]
y_data = [100, 400, 900]

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
#ax1.bar(x_years, y_data)
#ax2.bar(x_years, y_data)
#ax3.bar(x_years, y_data)
#ax4.bar(x_years, y_data)


ax1.bar(x_years, y_data, color = "aquamarine", edgecolor = "black", hatch="/")
ax2.bar(x_years, y_data, color = "salmon", edgecolor = "black", hatch="\\")
ax3.bar(x_years, y_data, color = "navajowhite", edgecolor = "black", hatch="+")
ax4.bar(x_years, y_data, color = "lightskyblue", edgecolor = "black", hatch="8")

plt.tight_layout()

plt.show() """


#=====================================================================

# seaborn

""" tips = sns.load_dataset("tips")

sns.regplot(x="total_bill", y="tip", data=tips)

plt.show()
 """


# 지표별 상관관계

""" tips = sns.load_dataset("tips")
print(tips)

plt.figure(figsize=(10, 6))

#sns.barplot(x="day", y="total_bill", data=tips)
#sns.barplot(x="day", y="total_bill", data=tips, palette="viridis")
#sns.barplot(x="tip", y="total_bill", data=tips)
#sns.barplot(x="sex", y="total_bill", data=tips)
#sns.barplot(x="sex", y="tip", data=tips)
#sns.barplot(x="smoker", y="total_bill", data=tips)
#sns.barplot(x="smoker", y="tip", data=tips)
#sns.barplot(x="time", y="total_bill", data=tips)

plt.title("Average Tips")
plt.xlabel("x")
plt.ylabel("Average")

plt.show() """


# 타이타닉 예제

""" titanic = sns.load_dataset("titanic")
print(titanic)

#sns.countplot(x="class", hue="who", data=titanic)
#sns.countplot(x="class", hue="alive", data=titanic)
#sns.countplot(x="sex", hue="alive", data=titanic)
#sns.countplot(x="alone", hue="who", data=titanic)

#sns.barplot(x="embark_town", y="survived", hue="pclass", data=titanic)
#sns.barplot(x="sex", y="survived", hue="pclass", data=titanic)

plt.show() """


# 주식 데이터 분석 

df = fdr.DataReader("KS11")
df0 = df.loc["2023"]

print(df0)

df0["Open"].plot()
df0["High"].plot()
df0["Low"].plot()
df0["Close"].plot()

plt.grid(True)
plt.show()











