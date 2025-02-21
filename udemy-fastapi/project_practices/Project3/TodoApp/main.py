from fastapi import FastAPI
from database import engine
from routers import auth, todos
from fastapi.middleware.cors import CORSMiddleware
import models

app = FastAPI()

# Allow all origins for CORS
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create all tables in the database
models.Base.metadata.create_all(bind=engine)

# Include the routers for the auth and todos APIs
app.include_router(auth.router)
app.include_router(todos.router)

# Automatically generated OpenAPI schema will include all the operations
