from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from app.domain.entities.random_string import RandomStringRequest, RandomStringResponse
from app.utils.random_string import RandomStringGenerator
from app.domain.exceptions.characters_not_available import CharactersNotAvailableException

router = APIRouter(prefix="/random-string")

@router.get("/")
async def get_random_string(request: RandomStringRequest= Depends()) -> RandomStringResponse:


    random_strings = RandomStringGenerator.generate_multiple(
        length=request.length,
        count=request.number_of_strings,
        add_lowercase=request.use_lowercase,
        add_uppercase=request.use_uppercase,
        add_numbers=request.use_numbers,
        add_special_characters=request.use_special_characters
    )

    return RandomStringResponse(random_strings=random_strings)
    