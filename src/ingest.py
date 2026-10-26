import pandas as pd
import requests
import time

# 1. Plug in target session key 
session_key = 9158

# 2. List the core relational endpoints to fetch
endpoints = ["sessions", "drivers", "laps", "pit", "weather", "session_result"]

print(f"Starting F1 pipeline extraction for session {session_key}...\n")

for endpoint in endpoints:
  # Dynamically build the URL using the session key
  url = f"https://api.openf1.org/v1/{endpoint}?session_key={session_key}"

  try:
    response = requests.get(url)

    if response.status_code == 200:
      data = response.json()
      if data:
        # Convert JSON data into a pandas DataFrame
        df = pd.DataFrame(data)

        # Save to a local CSV file
        file_name = f"{endpoint}.csv"
        df.to_csv(file_name, index=False)
        print(f"Saved {len(df)} rows to {file_name}")
      else:
        print(f"No data returned for '{endpoint}' in this session.")
    else:
      print(
          f"Failed to fetch '{endpoint}'. Status code:"
          f" {response.status_code}"
      )

      time.sleep(1)

  except Exception as e:
    print(f"Error with '{endpoint}': {e}")

print(
    "\n Pipeline extraction complete! Your CSV files are ready for your"
    " database."
)