from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello, FastAPI!"}
# Change made remotely
# Learning Git and GitHub
# Practicing Git commands
# This change is only on my feature branch
# Change made on main before rebase
# Cherry-pick this change
