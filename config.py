# config.py
from dotenv import load_dotenv
import os
from sqlalchemy import create_engine

load_dotenv()  # load .env variables

# Get the PostgreSQL connection URL from .env
engine = create_engine(os.getenv("SUPABASE_DB_URL"))
