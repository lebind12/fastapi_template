from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

# cors origin setting area
origins = [
    "http://127.0.0.1:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# below function is helloworld
# use 'router' in fastapi
@app.get("/")
def hello():
    return {"hello": "world"}