from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from endpoints import cities, schools, vacancies
import uvicorn

api = FastAPI(title='API вакансий schoolrm.ru',
              version=0.1)

origins = ["*"]

api.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# endpoints
api.include_router(cities.router, tags=['Районы'], prefix='/cities')
api.include_router(schools.router, tags=['Школы'], prefix='/schools')
api.include_router(vacancies.router, tags=['Вакансии'], prefix='/vacancies')


if __name__ == '__main__':
    uvicorn.run('api:api',
                port=8888,
                reload=True)