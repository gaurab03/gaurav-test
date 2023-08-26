from fastapi import FastAPI
from app.api.v1.endpoints.userDetails import router as root_router

app = FastAPI()

app.include_router(root_router)
