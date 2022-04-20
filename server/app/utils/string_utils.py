from datetime import datetime


months_dict = {'января': 1, 'февраля': 2, 'марта': 3, 'апреля': 4, 'мая': 5, 'июня': 6,
               'июля': 7, 'августа': 8, 'сентября': 9, 'октября': 10, 'ноября': 11, 'декабря': 12}


def str_to_date(s: str):
    date_items = s.split()
    time_items = date_items[3][:1].split(':')

    year = int(date_items[2])
    month = months_dict[date_items[1]]
    day = int(date_items[0])

    hour = int(time_items[0])
    minute = int(time_items[1])

    return datetime(year, month, day, hour, minute)
