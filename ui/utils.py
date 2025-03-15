from datetime import datetime

import pandas as pd


def process_data(data):
    """Convert list of dictionaries into a Pandas DataFrame with formatted timestamps."""
    try:
        df = pd.DataFrame(data)

        # Convert Unix timestamp to readable datetime
        df["timestamp"] = df["timestamp"].apply(lambda x: datetime.fromtimestamp(x).strftime("%Y-%m-%d %H:%M:%S"))

        return df
    except Exception as e:
        return pd.DataFrame()