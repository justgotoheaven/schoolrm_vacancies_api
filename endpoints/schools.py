from fastapi import APIRouter, Response, status
from core.schools import Schools
from schemas import School, SchoolMin
from typing import Optional, List

router = APIRouter()

@router.get('/get_all',
            tags=['Школы'],
            name='Получить список школ по району',
            response_model=Optional[List[SchoolMin]])
def get_schools(city: int, response: Response):
    """
    Возвращает список школ по району с доменами на сайте schoolrm.ru
    """
    data_rep = Schools()
    data = data_rep.get_schools_by_city(city)
    if data is None:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return None
    return data


@router.get('/get_by_domain',
            tags=['Школы'],
            name='Получить информацию о школе по домену',
            response_model=Optional[School])
def get_school_by_domain(domain: str, response: Response):
    """
    Возвращает информацию о школе
    """
    data_rep = Schools()
    school = data_rep.get_one_school(domain)
    if school is None:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return None
    return school

