from fastapi import FastAPI

# Initialize FastAPI app
app = FastAPI()


# Define routes
@app.get("/")
def read_root():
    return {"message": "This is a sample FastAPI application."}


# Get responses from query parameters
@app.get("/char_count/")
def count_chars(inputstr: str = "Hello"):
    # Count the number of characters in the input string
    return {"message": f"The input string '{inputstr}' has {len(inputstr)} characters."}


@app.get("/items/{item_id}")
def read_item(item_id: int):
    items = {1: "Item One", 2: "Item Two", 3: "Item Three"}
    if item_id not in items:
        return {"error": "Item not found"}
    else:
        return {"message": items[item_id]}
