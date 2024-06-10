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
    return {"message": "Saludos desde app!"}

# http://127.0.0.1:8000/article/?url=https://www.df.cl/economia-y-politica/macro/las-senales-economicas-en-mayo-se-modera-el-interes-por-el-consumo
@app.get('/article/')
async def getArticle(url: str):
    response = articleScrapper(url)
    return response

