from fastapi import APIRouter, Response, status
from typing import List
from schemas import Vacancy
from core.vacancies import Vacancies

router = APIRouter()

@router.get('/get_by_school',
            response_model=List[Vacancy],
            name='Получить вакансии школы')
def get_vacancies_by_school(school_domain: str, response: Response):
    """
    Возвращает список вакансий школы
    """
    data_rep = Vacancies()
    data = data_rep.get_vacancies(school_domain)
    if data is None:
        response.status_code = status.HTTP_404_NOT_FOUND
        return None
    return data
