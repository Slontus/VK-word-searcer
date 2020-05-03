import requests
import datetime
import chart_studio
import plotly.graph_objects as go
from dotenv import load_dotenv
import os
import logging

API_VK = "https://api.vk.com/method/"
VERSION = "5.58"
METHOD_SEARCH = "newsfeed.search"
RESULTS = 200
SEARCH = 'кока-кола'
PERIOD = 7


def provide_time_stamps(period):
    _days = []
    today = datetime.date.today()
    for day in range(period):
        current_day = today - datetime.timedelta(days=day)
        day_before = today - datetime.timedelta(days=(day + 1))
        start_time = datetime.datetime(*day_before.timetuple()[:3]).timestamp()
        end_time = datetime.datetime(*current_day.timetuple()[:3]).timestamp()
        _days.append((day_before, start_time, end_time))
    return _days


def get_statistic(token, period):
    statistics = []
    for day, start_time, end_time in provide_time_stamps(period):
        payload = {
                   'access_token': token,
                   'v': VERSION,
                   'count': RESULTS,
                   'q': SEARCH,
                   'start_time': start_time,
                   'end_time': end_time,
                   }
        url = "".join([API_VK, METHOD_SEARCH])
        try:
            response = requests.get(url, params=payload)
            response.raise_for_status()
            posts = response.json()
            if 'error' in posts:
                raise requests.exceptions.HTTPError(posts['error']['error_msg'])
        except requests.exceptions.HTTPError as _error:
            raise requests.exceptions.HTTPError(f"Not possible to get statistic: {_error}")
        else:
            total_count = posts['response']['total_count']
            statistics.append((day, total_count))
    return statistics


if __name__ == "__main__":
    logging.basicConfig(format="[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s] %(message)s",
                        level=logging.DEBUG, filename='log.log')
    try:
        load_dotenv()
        username = os.getenv("USER")
        api_key = os.getenv("API_KEY")
        access_token = os.getenv("ACCESS_TOKEN")
        chart_studio.tools.set_credentials_file(username=username, api_key=api_key)
        statistic = get_statistic(access_token, PERIOD)
        days, times_appeared = list(zip(*statistic))
        fig = go.Figure([go.Bar(x=days, y=times_appeared)])
        chart_studio.plotly.plot(fig, filename='coca_cola_statistic', auto_open=True)
    except requests.exceptions.HTTPError as error:
        logging.error(error)
    finally:
        logging.error("Test")
