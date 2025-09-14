import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("cfb23.csv")

df["Team"] = df["Team"].str.split("(", expand=True)[0].str.strip()
print(df["Team"])

#Calc win percentage
df[["Wins", "Losses"]] = df["Win-Loss"].str.split("-", expand=True)
df["Wins"] = df["Wins"].astype(int)
df["Losses"] = df["Losses"].astype(int)
df["Games"] = df["Games"].astype(int)
df["Win %"] = df["Wins"] / df["Games"]*100

# === Function to show team summary ===
def team_summary(team_name):
    team_data = df[df['Team'] == team_name]
    if team_data.empty:
        print(f"Could not find {team_name}")
    else:
        print(f"\n--- {team_name} Season Summary ---")
        print(team_data.T)


team_summary("LSU")
