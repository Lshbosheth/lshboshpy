from fastapi import APIRouter, Query
from typing import List, Union
import random
from datetime import datetime, timedelta
from . import constant

router = APIRouter(
    prefix="/idCard",
    tags=["idCard"],
    responses={404: {"description": "Not found"}},
)


class IdNumber(str):
    def __init__(self, id_number):
        super(IdNumber, self).__init__()
        self.id = id_number
        self.area_id = int(self.id[0:6])
        self.birth_year = int(self.id[6:10])
        self.birth_month = int(self.id[10:12])
        self.birth_day = int(self.id[12:14])

    def get_area_name(self):
        return constant.AREA_INFO[self.area_id]

    def get_birthday(self):
        return "{0}-{1}-{2}".format(self.birth_year, self.birth_month, self.birth_day)

    def get_age(self):
        now = (datetime.now() + timedelta(days=1))
        year, month, day = now.year, now.month, now.day
        if year == self.birth_year:
            return 0
        else:
            if self.birth_month > month or (self.birth_month == month and self.birth_day > day):
                return year - self.birth_year - 1
            else:
                return year - self.birth_year

    def get_sex(self):
        return int(self.id[16:17]) % 2

    def get_check_digit(self):
        check_sum = 0
        for i in range(0, 17):
            check_sum += ((1 << (17 - i)) % 11) * int(self.id[i])
        check_digit = (12 - (check_sum % 11)) % 11
        return check_digit if check_digit < 10 else 'X'

    @classmethod
    def generate_id(cls, sex=0):
        id_number = str(random.choice(list(constant.AREA_INFO.keys())))
        start, end = datetime.strptime("1960-01-01", "%Y-%m-%d"), datetime.strptime("2000-12-30", "%Y-%m-%d")
        birth_days = datetime.strftime(start + timedelta(random.randint(0, (end - start).days + 1)), "%Y%m%d")
        id_number += str(birth_days)
        id_number += str(random.randint(10, 99))
        id_number += str(random.randrange(sex, 10, step=2))
        return id_number + str(cls(id_number).get_check_digit())


@router.get("/")
async def read_items():
    random_sex = random.randint(0, 1)  # 随机生成男(1)或女(0)
    return IdNumber.generate_id(random_sex)
