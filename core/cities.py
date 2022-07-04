from typing import List
from schemas import City
from core.base import BaseParser
from config import Config


class Cities(BaseParser):

    def get_cities_list(self) -> List[City]:
        response = self.session.get(Config.ROOT_URL)
        self.soup = self.get_soup(response.text)
        schools_selection_div = self.soup.find('div', attrs={'class': 'departments__choose-block',
                                                        'data-item': 'tab_960'})
        select_element = schools_selection_div.find('select', id='departments-region-select')
        data = list()
        for option in select_element.find_all('option')[1:]:
            current_city = City(name=option.text,
                                code=int(option['value']))
            data.append(current_city)
        return data
