from pyrogram import Client

print("Pyrogram V2 Session String Generator")
API_ID = input("Enter API ID: ")
API_HASH = input("Enter API HASH: ")

with Client(name="USS", api_id=API_ID, api_hash=API_HASH, in_memory=True) as app:
    print(app.export_session_string())  # Add parentheses to call the method
