import pandas as pd
import requests
from datetime import datetime
from sqlalchemy import create_engine
import os

def get_crypto_data(vs_currency="usd", coins=["bitcoin", "ethereum", "dogecoin"]):
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": vs_currency,
        "ids": ','.join(coins),
        "order": "market_cap_desc",
        "per_page": len(coins),
        "page": 1,
        "sparkline": False
    }

    try:
        response = requests.get(url, params=params)
        data = response.json()
        if not isinstance(data, list) or len(data) == 0:
            print("⚠️ No data received.")
            return pd.DataFrame()

        df = pd.DataFrame(data)[[
            'id', 'symbol', 'name', 'current_price',
            'price_change_percentage_24h', 'market_cap', 'total_volume'
        ]]
        df.rename(columns={
            "id": "coin_id",
            "current_price": "price_usd",
            "price_change_percentage_24h": "change_24h",
            "market_cap": "market_cap",
            "total_volume": "volume_24h"
        }, inplace=True)

        df['timestamp'] = pd.Timestamp.utcnow()
        df['source_type'] = 'live'
        return df
    except Exception as e:
        print("❌ API error:", e)
        return pd.DataFrame()

def store_data(df):
    if df.empty:
        print("⚠️ Skipped insert: DataFrame is empty")
        return

    engine = create_engine(
        f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
    )
    df.to_sql(name="prices", con=engine, if_exists="append", index=False)
    print(f"✅ Stored {len(df)} rows at {datetime.utcnow()}")

if __name__ == "__main__":
    df = get_crypto_data()
    store_data(df)
