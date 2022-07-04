from typing import Optional, List
from schemas import Vacancy
from core.base import BaseParser
from config import Config


class Vacancies(BaseParser):

    def get_vacancies(self, school_domain: str) -> List[Vacancy]:
        res = self.session.post(Config.GET_VACANCIES_URL.format(school_domain))
        self.soup = self.get_soup(res.text)
        block = self.soup.find('div', id='center_block')
        vacancies = list()
        vac_list = block.find_all('td', class_='first_td')
        if not vac_list:
            return None
        for vac in vac_list:
            cur_vacancy = Vacancy(vacancy=vac.text)
            vacancies.append(cur_vacancy)
        return vacancies

