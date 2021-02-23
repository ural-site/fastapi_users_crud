from fastapi import FastAPI

app = FastAPI()


@app.get("/users")
def find_all_users():
    print("111")
    return "List all user"
