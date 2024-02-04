# from typing import Union
# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# def read_root():
#     return {"Hello": "World"}

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}

from fastapi import FastAPI, HTTPException
from typing import List

app = FastAPI()

# Sample data folder path
data_folder = "D:/PROJECT/PyMosaicAPI/JSON_data"

# Helper function to read JSON files
def read_json_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = file.read()
        return data
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="File not found")

# Helper function to write data to JSON files
def write_json_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)

# GET Request - Read data from JSON file
@app.get("/{filename}")
def read_data(filename: str):
    file_path = f"{data_folder}{filename}"
    data = read_json_file(file_path)
    return {"filename": filename, "data": data}


from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import Optional
import bcrypt

app = FastAPI()

# Dummy database (in-memory)
fake_db = {}

# User model
class User(BaseModel):
    username: str
    password: str

# Utility function for hashing passwords
def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

# Utility function to verify password
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))

@app.post("/register/")
def register_user(user: User):
    # Check if user already exists
    if user.username in fake_db:
        raise HTTPException(status_code=400, detail="Username already registered")

    # Hash user's password before storing it
    hashed_password = hash_password(user.password)
    fake_db[user.username] = hashed_password

    return {"username": user.username, "message": "User registered successfully"}
#write the code here
# You can add more endpoints here for login, user profile, etc.
