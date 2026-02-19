from fastapi import FastAPI

app = FastAPI(title="Auth Service")

@app.get("/")
def root():
    return {"message": "Auth Service is running"}

@app.get("/hello")
def hello():
    return {"message": "Hello from Auth Service"}
