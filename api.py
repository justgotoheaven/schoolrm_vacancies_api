from fastapi import FastAPI
from endpoints import cities, schools, vacancies
import uvicorn

api = FastAPI(title='API вакансий schoolrm.ru',
              version=0.1)

# endpoints
api.include_router(cities.router, tags=['Районы'], prefix='/cities')
api.include_router(schools.router, tags=['Школы'], prefix='/schools')
api.include_router(vacancies.router, tags=['Вакансии'], prefix='/vacancies')


if __name__ == '__main__':
    uvicorn.run('api:api',
                port=8080,
                reload=True)