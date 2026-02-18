from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# 1. THE SCHEMA: Define what an 'Expense' looks like
class Expense(BaseModel):
    item: str
    price: float
    category: str = "General"

# 2. THE DATA: A temporary list to act as our database
fake_database = []

@app.get("/")
def home():
    return {"status": "AI Expense Tracker is Live!"}

@app.post("/add-expense")
def add_expense(data: Expense):
    fake_database.append(data)
    return {"message": f"Successfully added {data.item}", "current_count": len(fake_database)}