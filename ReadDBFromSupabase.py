import os
from dotenv import load_dotenv
from supabase import create_client

# Load environment variables from .env file
load_dotenv("supabasedb.env")

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

# Initialize the Supabase client
supabase = create_client(url, key)

# Read/select data from your table
response = supabase.table("customer_order").select("*").execute()

# Print the retrieved data
print(response.data)
