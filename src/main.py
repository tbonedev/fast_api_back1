
from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.database import delete_tables, create_tables

from src.router import router as tasks_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("База Очищена")
    await create_tables()
    print("База Готова до роботи")
    yield
    print("Виключення")

app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)




