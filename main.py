import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("cfb23.csv")

#Calc win percentage
df[["Wins", "Losses"]] = df["Win-Loss"].str.split("-", expand=True)
df["Wins"] = df["Wins"].astype(int)
df["Losses"] = df["Losses"].astype(int)
df["Games"] = df["Games"].astype(int)
df["Win %"] = df["Wins"] / df["Games"]*100


