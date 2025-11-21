from fastapi import FastAPI
from fastapi.responses import JSONResponse
from app.api import router as api_router

from app.domain.exceptions.characters_not_available import CharactersNotAvailableException

app = FastAPI()

@app.exception_handler(CharactersNotAvailableException)
async def characters_not_available_exception_handler(request, exc):
    return JSONResponse(
        status_code=400,
        content={"message": "Недостаточно символов для генерации строки (все группы символов отмечены, как false)."},
    )

app.include_router(api_router)