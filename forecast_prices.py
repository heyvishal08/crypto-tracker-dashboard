import pandas as pd
from prophet import Prophet
from sqlalchemy import create_engine
import os
from datetime import datetime
import warnings

warnings.filterwarnings("ignore")

engine = create_engine(
    f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
)

forecast_days = 7
coins = ["bitcoin", "ethereum", "dogecoin"]

for coin in coins:
    print(f"\n🔮 Forecasting: {coin}")

    query = f"""
        SELECT timestamp, price_usd FROM prices
        WHERE coin_id = '{coin}'
        AND source_type IN ('historical', 'live')
        ORDER BY timestamp
    """
    df = pd.read_sql(query, engine)

    if df.empty or len(df) < 30:
        print(f"⚠️ Not enough data for {coin}. Skipping.")
        continue

    df = df.rename(columns={"timestamp": "ds", "price_usd": "y"})
    model = Prophet(daily_seasonality=True)
    model.fit(df)

    future = model.make_future_dataframe(periods=forecast_days)
    forecast = model.predict(future)

    result = forecast[['ds', 'yhat']].tail(forecast_days)
    result["coin_id"] = coin
    result["symbol"] = coin[:3]
    result["name"] = coin.capitalize()
    result["change_24h"] = None
    result["market_cap"] = None
    result["volume_24h"] = None
    result["source_type"] = "forecast"
    result = result.rename(columns={"ds": "timestamp", "yhat": "price_usd"})

    try:
        result.to_sql(name="prices", con=engine, if_exists="append", index=False)
        print(f"✅ Forecast stored for {coin}")
    except Exception as e:
        print("❌ Insert error:", e)
