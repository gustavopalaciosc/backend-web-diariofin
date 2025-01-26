from fastapi import FastAPI, Request
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from starlette.responses import JSONResponse
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


limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter


@app.exception_handler(RateLimitExceeded)
async def rate_limit_exceeded_handler(request: Request, exc: RateLimitExceeded):
    return JSONResponse(
        status_code=429,
        content={"status_code": 429, "message": "Servidor sobrecargado. Vuelva a intentar más tarde."},
    )

@app.get('/')
async def get():
    return {'status_code': 200, 'message': "Saludos desde app!"}


@app.get('/article/', status_code=200)
@limiter.limit('30/minute')
async def getArticle(request: Request, url: str):
    response = await articleScrapper(url)
    print(response["image_url"])
    return response

