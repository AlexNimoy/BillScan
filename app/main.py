from fastapi import FastAPI
from .routers import text_extraction_router

app = FastAPI()

# Подключение роутеров
app.include_router(text_extraction_router.router)
