from .base_domain_exception import BaseDomainException

class CharactersNotAvailableException(BaseDomainException):
    """Невозможно сгенерировать строку с заданными параметрами из-за недостатка доступных символов."""
    pass