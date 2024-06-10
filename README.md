# API Articulos Diario Financiero
API creada para la app web de articulos del Diario Financiero gratuitos.


## SetUp
```
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Funcionamiento

Estructura de GET requests: http://127.0.0.1:8000/article/?url=url_articulo