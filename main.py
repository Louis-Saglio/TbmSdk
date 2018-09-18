import datetime
from typing import List

import requests


def convert_to_datetime(date: str):
    return datetime.datetime.strptime(date.split("+")[0], "%Y-%m-%dT%H:%M:00")


def get_next_visit_time(data: dict) -> List[datetime.datetime]:
    result = []
    for a in data["schedules"]["datetimes"].values():
        for b in a:
            next_time = convert_to_datetime(b["datetime"])
            if next_time > datetime.datetime.now():
                result.append(next_time)
    return result


def get_salengro_to_ccdulac():
    # todo : généraliser cette fonction pour avoir n'importe quel arrêt et n'importe quelle direction
    data = requests.get(
        "https://ws.infotbm.com/ws/1.0/stop-points-informations/route:TBC:15/stop_point:TBC:SP:3189"
    ).json()
    return get_next_visit_time(data)


def show_next_visit(number=2):
    times = get_salengro_to_ccdulac()[:number]
    for time in times:
        print(time.strftime("%Hh %M"))


if __name__ == "__main__":
    show_next_visit()
