import random
import string

class RandomStringGenerator:

    def generate(length: int, 
                 add_lowercase: bool = True,
                 add_special_characters: bool = False, 
                 add_numbers: bool = False,
                 add_uppercase: bool = False,
                 characters = None) -> str:

        if characters is None:
            characters = ""        
            if add_lowercase:
                characters += string.ascii_lowercase
            if add_special_characters:
                characters += string.punctuation
            if add_numbers:
                characters += string.digits
            if add_uppercase:
                characters += string.ascii_uppercase
            
            if not characters:
                characters = string.ascii_lowercase

        return ''.join(random.choice(characters) for _ in range(length))
    
    def generate_multiple(length: int, 
                          count: int,
                          add_lowercase: bool = True,
                          add_special_characters: bool = False, 
                          add_numbers: bool = False,
                          add_uppercase: bool = False,
                          characters = None) -> list[str]:

        return [RandomStringGenerator.generate(length, 
                                               add_lowercase,
                                               add_special_characters, 
                                               add_numbers,
                                               add_uppercase,
                                               characters) for _ in range(count)]