from fastapi import FastAPI
from .routers.lessons import router as lessons_router
from .routers.search import router as search_router
#from routers import lessons

app = FastAPI()
app.include_router(lessons_router)
#app.include_router(lessons.router) 

app.include_router(search_router)

@app.get("/")
def root():
    return {"message": "Bem-vindo a API de suas aulas"}