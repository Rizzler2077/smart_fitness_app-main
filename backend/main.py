from fastapi import FastAPI

app = FastAPI()

@app.get("/ping")
def ping():
    return {"msg": "pong"}

@app.get("/users")
def get_users():
    return [{"id": 1, "name": "Test User"}]

@app.get("/workouts")
def get_workouts():
    return [{"id": 1, "name": "Push-ups", "duration": "10 mins"}]
