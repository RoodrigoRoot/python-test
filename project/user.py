from __future__ import annotations
import uuid
from typing import Union


class User:
    """
    
    """

    def __init__(self, name: str, username: str, age: int) -> None:
        self.id = uuid.uuid4()
        self.name = ValidationUser.validate_name(name)
        self.username = ValidationUser.validate_username(username)
        self.age = ValidationUser.validate_age(age)

    def __str__(self) -> str:
        return f"ID: {self.id}\nName: {self.name}\nUsername: {self.username}\nAge: {self.age}\n"

    def create(self) -> User:
        self.save_user_file(self)
        return self

    def save_user_file(self, user: User) -> bool:
        try:
            with open("users.txt", "a+") as file:
                file.write(str(user) + "\n")
                return True
        except Exception:
            return False


class ValidationUser:

    @classmethod
    def validate_username(cls, username: str) -> str:
        if not ValidationUser.is_blank(username):
            raise ValueError("El campo Username, no puede estar vacío")
        if len(username) >= 30:
            raise ValueError("El campo Username, no puede ser mayor de 30 caracteres")
        if len(username) < 4:
            raise ValueError("El campo Username, no puede ser menor de 4 caracteres")

        return username

    @classmethod
    def validate_name(cls, name: str) -> str:
        if not ValidationUser.is_blank(name):
            raise ValueError("El campo Nombre, no puede estar vacío")
        if len(name) > 50:
            raise ValueError("El campo Username, no puede ser mayor de 50 caracteres")
        if not name.isalpha():
            raise ValueError("El nombre no es válido")
        return name

    @classmethod
    def validate_age(cls, age: int) -> int:
        if not ValidationUser.is_blank(age):
            raise ValueError("El campo Edad, no puede estar vacío o tener un 0")
        if not isinstance(age, int):
            raise ValueError("Solo se aceptan números")
        if age < 0:
            raise ValueError("No se aceptan números negativos")
        if age < 18:
            raise ValueError("Debes ser mayor de 18 años")

        return age

    @classmethod
    def is_blank(cls, value: Union[str, int])-> bool:
        if value:
            return True
        return False
