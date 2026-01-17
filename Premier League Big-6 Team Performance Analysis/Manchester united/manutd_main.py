from heapq import nlargest

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mplsoccer import Pitch

# reading sheet
df=pd.read_csv("Manchester_United_2025_26_-_Sample_Stats.csv")


#replacing blank space with "_"
df["Player"]=df["Player"].str.replace(" ","_")



#matplotlib
#pie chart of players position
plt.figure()
Count=df["Position"].value_counts()

plt.title("Man Utd",fontsize=20,fontweight="bold",y=1)
plt.suptitle("Player Count",fontsize=16,fontweight="bold",y=0.10)

plt.pie(Count.values,
        labels=Count.values,
        colors=["Green","Blue","orange","red"],
        )
plt.legend(["MID","FWD","DEF","GK"],loc="upper left",bbox_to_anchor=(-0.15,1))


#bar chart :- most minutes played
plt.figure()
Minutes=df.nlargest(5,"Minutes_Played")[["Player","Minutes_Played"]]

plt.bar(Minutes["Player"],Minutes["Minutes_Played"])
plt.xticks(
     ticks=range(5),
     labels=["Bruno","Onana","Rashford","Dalot","De_ligt"])

plt.title("Most Minutes Played",fontsize=20,fontweight="bold")
plt.xlabel("Player",fontsize=12,fontweight="bold")
plt.ylabel("Minutes",fontsize=12,fontweight="bold")


#bar chart :- Most goals
plt.figure()
Goals=df.nlargest(5,"Goals")[["Player","Goals"]]
plt.bar(Goals["Player"],Goals["Goals"],
        color="#f7c301")
plt.title("Most Goals",fontsize=20,fontweight="bold")
plt.xlabel("Player",fontsize=12,fontweight="bold",labelpad=5)
plt.ylabel("Goals",fontsize=12,fontweight="bold",labelpad=10)
plt.xticks(
     ticks=range(5),
     labels=["Rashford","Hojlund","Bruno","Garnacho","Zirkzee"])


#conversion rate
plt.figure()
df["Chance"]=df["Goals"]/df["Shots_On_Target"]
df["Chance"]=df["Chance"].replace([np.inf,-np.inf],np.nan)
df["Chance"]=df["Chance"].fillna(df["Chance"].mean())
High_Conversion=df.nlargest(5,"Chance")[["Player","Chance"]]


plt.bar(High_Conversion["Player"],High_Conversion["Chance"],color="#be2d2d")
plt.title("Goal Conversion Rate",fontsize=20,fontweight="bold")
plt.xlabel("Player",fontsize=12,fontweight="bold")
plt.ylabel("Chance",fontsize=12,fontweight="bold")
plt.xticks(
     ticks=range(5),
     labels=["De_Ligt","Varane","Mainoo","Casemiro","Hojlund"])


#Top playermaker
plt.figure(figsize=(12,8))
plt.scatter(df["Pass_Accuracy"],df["Passes"],s=100)

for _, row in df.iterrows():
    plt.annotate(
    row["Player"],
    (row["Pass_Accuracy"], row["Passes"]),
    textcoords="offset points",
    xytext=(6,6),
    fontsize=10)


plt.title("Top Playmakers",fontweight="bold",fontsize=20)
plt.xlabel("Pass Accuracy",fontsize=12,fontweight="bold",labelpad=10)
plt.ylabel("Passes",fontsize=12,fontweight="bold",labelpad=10)
plt.grid(alpha=0.3)
plt.xlim(70,100)
plt.ylim(0,2500)


#top G+A
plt.figure()
df["GA"]=df["Goals"]+df["Assists"]
top5GA=df.nlargest(5,"GA")[["Player","GA"]]

plt.bar(top5GA["Player"],top5GA["GA"],color="grey")
plt.xticks(
     ticks=range(5),
     labels=["Bruno","Rashford","Hojlund","Garnacho","Zirkzee"])

plt.title("Top 5 G+A",fontsize=20,fontweight="bold")
plt.xlabel("Players",fontsize=12,fontweight="bold",labelpad=5)
plt.ylabel("G+A",fontsize=12,fontweight="bold",labelpad=10)




#shots on pitch
pitch=Pitch(
    pitch_type="statsbomb",
    line_color="white",
    pitch_color="lightgreen"
)

fig,ax=pitch.draw(figsize=(10,14))

shots=df[["Shot_X","Shot_Y"]].dropna()

pitch.scatter(df["Shot_X"],df["Shot_Y"],
              ax=ax,color="white",s=80)

plt.title("Shot on Pitch",fontweight="bold",fontsize=40,pad=20)


# heatmap average position
pitch=Pitch(
     pitch_type="statsbomb",
     line_color="white",
     pitch_color="lightgreen"
 )

fig,ax=pitch.draw(figsize=(10,14))

pitch.kdeplot(df["Avg_X"],df["Avg_Y"],ax=ax,fill=True,
              bw_adjust=0.4,
              levels=120,
              thresh=0.05,
              cmap="inferno",
              alpha=0.9
              )

plt.title("Average Position",fontsize=40,fontweight="bold",pad=20)


plt.show()
df.to_csv("Manchester_United_2025_26_-_Sample_Stats.csv",index=False)
