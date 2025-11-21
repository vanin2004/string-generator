from pydantic import BaseModel, Field, model_validator
from app.domain.exceptions.characters_not_available import CharactersNotAvailableException

class RandomStringRequest(BaseModel):
    """Модель запроса для генерации случайной строки."""
    length: int = Field(gt=0, lt=100, default=8, description="Количество символов в случайной строке")
    use_lowercase: bool = Field(default=True, description="Использовать строчные буквы")
    use_uppercase: bool = Field(default=False, description="Использовать заглавные буквы")
    use_numbers: bool = Field(default=False, description="Использовать цифры")
    use_special_characters: bool = Field(default=False, description="Использовать специальные символы")
    number_of_strings: int = Field(gt=0, lt=100 , default=1, description="Количество случайных строк для генерации")

    @model_validator(mode='after')
    def validate_any_characters_available(self) -> 'RandomStringRequest':
        if not (self.use_lowercase or self.use_uppercase or self.use_numbers or self.use_special_characters):
            raise CharactersNotAvailableException('Должен быть выбран хотя бы один тип символов для генерации строки')
        return self

class RandomStringResponse(BaseModel):
    """Модель ответа с сгенерированными случайными строками."""
    random_strings: list[str]