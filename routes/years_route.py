from fastapi import APIRouter
# from models.years_model import Year
import datetime

year_api_router = APIRouter()
a = datetime.datetime.now()

@year_api_router.get("/service/getage")
async def get_test(year:int):
    age = (a.year+543) - year
    return {"age": age}