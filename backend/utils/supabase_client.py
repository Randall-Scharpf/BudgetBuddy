from supabase import create_client
import os
from dotenv import load_dotenv

load_dotenv()
supabase_client = create_client(os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_KEY"))
