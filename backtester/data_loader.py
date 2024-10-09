 
# backtester/data_loader.py

import pandas as pd
import logging

def load_data(file_path):
    df = pd.read_csv(file_path)
    if df.empty:
        logging.error("Historical data is empty.")
    else:
        logging.info(f"Loaded {len(df)} data points.")
    df.sort_values('timestamp', inplace=True)
    df.reset_index(drop=True, inplace=True)
    return df.to_dict('records')  # Convert DataFrame to a list of dictionaries
