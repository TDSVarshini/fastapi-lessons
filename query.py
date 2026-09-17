@app.get("/search")
def search(name: str, age: int):
    return {
        "name": name,
        "age": age
    }