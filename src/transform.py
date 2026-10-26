import os
import pandas as pd


def transform_f1_data():
  # Create processed folder inside data/ if it doesn't exist
  os.makedirs("data/processed", exist_ok=True)

  endpoints = ["sessions", "drivers", "laps", "pit", "weather", "session_result"]

  for endpoint in endpoints:
    # Point to where raw CSVs are saved inside the data/ folder
    input_path = f"data/{endpoint}.csv"

    if not os.path.exists(input_path):
      print(f" Warning: {input_path} not found. Skipping.")
      continue

    print(f" Transforming {endpoint}...")

    # 1. Load data using pandas
    df = pd.read_csv(input_path)
    initial_rows = len(df)

    # 2. Clean nulls and duplicates
    df = df.drop_duplicates()

    # 3. Handle timestamps safely using clear naming
    for column_name in ["date", "date_start", "date_end"]:
      if column_name in df.columns:
        df[column_name] = pd.to_datetime(df[column_name], errors="coerce")

    # Drop rows if a critical session key is missing
    if "session_key" in df.columns:
      df = df.dropna(subset=["session_key"])

    # 4. Save to new processed folder
    output_path = f"data/processed/clean_{endpoint}.csv"
    df.to_csv(output_path, index=False)

    print(
        f" Success! {initial_rows} rows processed -> saved to {output_path}"
    )

  print(
      "\n Transformation complete! Your clean CSV files are ready in"
      " data/processed/."
  )


if __name__ == "__main__":
  transform_f1_data()