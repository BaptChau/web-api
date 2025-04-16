from fastapi import FastAPI
from .routers import news
app = FastAPI()
app.include_router(news.appRouter)

@app.get(path='/', name='root')
async def root_path():
    return {"message": "root path"}
