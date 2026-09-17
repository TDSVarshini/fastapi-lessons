from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello, FastAPI!"}

# Learning Git and GitHub
# Practicing Git commands# This change is only on my feature branch
