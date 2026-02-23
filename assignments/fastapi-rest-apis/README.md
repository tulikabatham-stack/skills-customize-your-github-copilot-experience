# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn to build modern, fast, and production-ready REST APIs using the FastAPI framework. You'll create a functional API with routes, request validation, and response models while understanding core concepts like routing, HTTP methods, and data validation.

## 📝 Tasks

### 🛠️ Create a Todo API

#### Description
Build a REST API for managing a simple todo list using FastAPI. The API should handle creating, retrieving, updating, and deleting todo items. Focus on implementing proper HTTP methods, request/response validation, and clear API documentation.

#### Requirements
Completed API should:

- Define Todo data model with fields for id, title, description, and completed status
- Implement GET endpoint to retrieve all todos
- Implement GET endpoint to retrieve a single todo by id
- Implement POST endpoint to create new todos with automatic id generation
- Implement PUT endpoint to update existing todos
- Implement DELETE endpoint to remove todos
- Use Pydantic models for request/response validation
- Include appropriate HTTP status codes (200, 201, 404, etc.)
- Have auto-generated API documentation accessible at `/docs`


### 🛠️ Add Error Handling and Validation

#### Description
Enhance your API with proper error handling, input validation, and meaningful error messages. Ensure the API gracefully handles edge cases and invalid requests.

#### Requirements
Completed program should:

- Validate required fields in POST/PUT requests
- Return 404 errors when attempting to access non-existent todos
- Prevent duplicate todo ids
- Include descriptive error messages in responses
- Handle edge cases like empty lists and invalid data types
- Use appropriate HTTP status codes for different error scenarios
