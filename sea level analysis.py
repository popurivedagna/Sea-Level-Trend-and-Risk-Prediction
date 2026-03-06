"""
Sea Level Trend and Risk Prediction
Author: POPURI SAI VEDAGNA

Description:
Analyzes sea level data to identify trends, detect dangerous levels,
and predict future sea levels using linear regression.
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
def load_data(file):

    df = pd.read_csv(file)

    df["date"] = pd.to_datetime(df["date"])
    df["sea_level"] = pd.to_numeric(df["sea_level"], errors="coerce")

    df = df.dropna()

def monthly_stats(df):

    df["month"] = df["date"].dt.to_period("M")

    stats = df.groupby("month")["sea_level"].agg(
        average="mean",
        maximum="max",
        minimum="min"
    )

    return stats
def extreme_levels(df):

    highest = df.loc[df["sea_level"].idxmax()]
    lowest = df.loc[df["sea_level"].idxmin()]

    return highest, lowest

def detect_danger(df, threshold=8):

    danger = df[df["sea_level"] >= threshold]

    return danger

def predict_future(df):

    df["days"] = (df["date"] - df["date"].min()).dt.days

    x = df["days"]
    y = df["sea_level"]

    slope, intercept = np.polyfit(x, y, 1)

    future_days = x.max() + 365
    predicted_level = slope * future_days + intercept

    return round(predicted_level, 2)

def plot_trend(df):

    df["days"] = (df["date"] - df["date"].min()).dt.days

    x = df["days"]
    y = df["sea_level"]

    slope, intercept = np.polyfit(x, y, 1)

    regression_line = slope * x + intercept

    plt.scatter(df["date"], y, label="Observed Levels")
    plt.plot(df["date"], regression_line, color="red", label="Trend Line")

    plt.title("Sea Level Trend Analysis")
    plt.xlabel("Date")
    plt.ylabel("Sea Level")

    plt.legend()
    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()
def main():

    file = "sea_level.csv"

    df = load_data(file)

    stats = monthly_stats(df)

    highest, lowest = extreme_levels(df)

    danger = detect_danger(df)

    prediction = predict_future(df)

    print("\n--- SEA LEVEL REPORT ---\n")

    print("Highest Sea Level:")
    print(highest)

    print("\nLowest Sea Level:")
    print(lowest)

    print("\nMonthly Statistics:")
    print(stats)

    print("\nDanger Level Days:")
    print(danger)

    print("\nPredicted Sea Level After 1 Year:", prediction)

    plot_trend(df)


if __name__ == "__main__":
    main()
