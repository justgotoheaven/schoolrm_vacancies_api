from fastapi import APIRouter
from core.cities import Cities
from schemas import City
from typing import List

router = APIRouter()

@router.get('/', response_model=List[City], name='Получить список районов')
def get_cities():
    """
    Возвращает список районов
    """
    data_repository = Cities()
    return data_repository.get_cities_list()

