import pandas as pd 
from tsfresh import extract_features
from tsfresh.utilities.dataframe_functions import impute


def main():

    # ==============================
    # LOAD DATA
    # ==============================
    df = pd.read_csv(
        r"C:\Users\jan\Downloads\archive\nyc_yellow_taxi_trip_records_from_Jan_to_Aug_2023.csv"
    )

    # SPEED FIX
    df = df.sample(n=50000, random_state=42) 

    # ==============================
    # DATETIME
    # ==============================
    df["tpep_pickup_datetime"] = pd.to_datetime(df["tpep_pickup_datetime"])
    df["tpep_dropoff_datetime"] = pd.to_datetime(df["tpep_dropoff_datetime"])

    df["trip_duration"] = (
        df["tpep_dropoff_datetime"] - df["tpep_pickup_datetime"]
    ).dt.total_seconds()

    # ==============================
    # HOURLY AGGREGATION
    # ==============================
    df["hour"] = df["tpep_pickup_datetime"].dt.floor("h")

    hourly = df.groupby("hour").agg({
        "trip_distance": "mean",
        "passenger_count": "mean",
        "fare_amount": "mean",
        "tip_amount": "mean",
        "total_amount": "mean",
        "trip_duration": "mean"
    }).reset_index()

    # CLEAN
    hourly = hourly.dropna()

    # ==============================
    # TSFRESH FORMAT
    # ==============================
    hourly = hourly.rename(columns={"hour": "time"})
    hourly["id"] = 1

    long_df = hourly.melt(
        id_vars=["id", "time"],
        var_name="kind",
        value_name="value"
    )

    # FINAL CLEAN
    long_df = long_df.dropna()

    # ==============================
    # FEATURE EXTRACTION
    # ==============================
    features = extract_features(
        long_df,
        column_id="id",
        column_sort="time",
        column_kind="kind",
        column_value="value",
        n_jobs=2
    )

    features = impute(features)

    print("Shape:", features.shape)
    print(features.head())

    features.to_csv("tsfresh_features.csv")


# ==============================
# REQUIRED ON WINDOWS
# ==============================
if __name__ == "__main__":
    main()