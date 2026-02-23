from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="Todo API", version="1.0.0")

# Define the Todo data model
class Todo(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False

# In-memory storage for todos (in production, use a database)
todos_db: List[Todo] = []

# TODO: Implement GET endpoint to retrieve all todos
# Route: GET /todos


# TODO: Implement GET endpoint to retrieve a single todo by id
# Route: GET /todos/{todo_id}


# TODO: Implement POST endpoint to create a new todo
# Route: POST /todos


# TODO: Implement PUT endpoint to update an existing todo
# Route: PUT /todos/{todo_id}


# TODO: Implement DELETE endpoint to remove a todo
# Route: DELETE /todos/{todo_id}


# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the Todo API"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
