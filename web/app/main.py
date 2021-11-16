import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

# CORS config
app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# read the variables
port = os.environ["PORT"]

@app.get("/")
async def index():
    print(f"port:{port}")
    response = {
        "server": "ecample server"
    }
    return response 

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=port)