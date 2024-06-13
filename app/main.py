from fastapi import FastAPI
from .utils.article_scrapper import articleScrapper
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
async def get():
    return {'status_code': 200, 'message': "Saludos desde app!"}


@app.get('/article/', status_code=200)
async def getArticle(url: str):
    response = articleScrapper(url)
    return response

