from pydantic import BaseModel
from typing import List


class City(BaseModel):
    name: str  # Имя города/района
    code:  int  # Код района


class SchoolMin(BaseModel):
    """
    Минимальная модель школы
    """
    name: str
    domain: str


class School(BaseModel):
    """
    Модель "Школа"
    """
    name: str  # Наименование
    domain: str  # Домен в системе schoolrm.ru
    address: str  # Адрес ОУ
    tel: str  # Информация о телефоне


class Vacancy(BaseModel):
    """
    Вакансии школы
    """
    vacancy: str  # Вакансия (должность)
