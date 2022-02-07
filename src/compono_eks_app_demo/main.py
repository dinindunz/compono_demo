from fastapi import FastAPI

app = FastAPI(title="Compono EKS App Demo")

@app.get("/")
def get_message():
    return {"message": "Compono EKS App Demo!"}