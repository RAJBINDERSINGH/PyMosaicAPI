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