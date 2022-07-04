from typing import Optional, List
from schemas import SchoolMin, School
from core.base import BaseParser
from config import Config


class Schools(BaseParser):

    def get_one_school(self, domain: str) -> Optional[School]:
        request_url = 'https://{}.schoolrm.ru'.format(domain)
        try:
            response = self.session.get(request_url)
            self.soup = self.get_soup(response.text)
            school_name = self.soup.find('div', class_='name_school').text.strip().replace('\n', ''). \
                replace('                        		', ' ')
            school_adr_and_phone = self.soup.find('div', class_='address_block')
            school_adr_pretty = school_adr_and_phone.text.strip().split('Телефон')[0]. \
                replace('            			                                        ', '').replace('Адрес:', '').strip()
            school_phone = school_adr_and_phone.text.split('Телефон:')[1].split('Контакты')[0].strip()
            school_data = School(name=school_name,
                                 domain=domain,
                                 address=school_adr_pretty,
                                 tel=school_phone)
        except:
            return None
        return school_data

    def get_schools_by_city(self, city: int) -> Optional[List[SchoolMin]]:
        data = dict(id=city)
        response = self.session.post(Config.GET_SCHOOLS_LIST_URL, data=data)
        if response.text == '':
            return None
        self.soup = self.get_soup(response.text)
        options = self.soup.find_all('option')[1:]
        schools = list()
        for option in options:
            cur_school = SchoolMin(name=option.text,
                                   domain=option['value'].split('.')[0])
            schools.append(cur_school)
        return schools
