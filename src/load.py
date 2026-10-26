import os
import pandas as pd
from sqlalchemy import create_engine

# 1. Define database connection string
DB_USER = "postgres"
DB_PASSWORD = "mysecretpassword"
DB_HOST = "127.0.0.1"
DB_PORT = "5432"
DB_NAME = "f1_warehouse"

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

def load_data():
    # 2. Create the SQLAlchemy engine
    engine = create_engine(DATABASE_URL)

    # Path to processed data folder
    processed_dir = "data/processed"

    if not os.path.exists(processed_dir):
        print(f"Directory {processed_dir} does not exist. Run your transformation script first!")
        return

    # Loop through all files in the processed directory
    for filename in os.listdir(processed_dir):
        if filename.endswith(".csv"):
            file_path = os.path.join(processed_dir, filename)
            table_name = f"f1_{filename.replace('.csv', '')}"
            
            print(f"Reading {filename}...")
            df = pd.read_csv(file_path)
            
            print(f"Writing {table_name} to database...")
            df.to_sql(table_name, engine, if_exists='replace', index=False, chunksize=10000)
            
            print(f"Successfully loaded {len(df)} rows into {table_name}.")

    print("\nAll data successfully loaded into PostgreSQL!")

if __name__ == "__main__":
    load_data()