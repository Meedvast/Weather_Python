import requests
import re
import csv
import glo

KEY = '&key=d53ea69f45304dd1bdd632ba6c39294c'
url_api = 'https://devapi.qweather.com/v7/weather/'
url_api_v2 = 'https://geoapi.qweather.com/v2/city/'


def get_location(api_type, city_kw='北京'):
    url_v2 = url_api_v2 + api_type + '?location=' + city_kw + KEY
    return requests.get(url_v2).json()


def get(api_type, city_id):
    url = url_api + api_type + '?location=' + city_id + KEY
    return requests.get(url).json()


def lookup_city(city_kw):
    city = get_location('lookup', city_kw)['location'][0]
    city_id = city['id']
    return city_id


def hourly(city_id):
    return get('24h', city_id)


def write_csv():
    print('请输入你想查询的城市:')
    city_kw = glo.text1
    city_id = lookup_city(city_kw)
    hourly_data = hourly(city_id)
    with open('weather.csv', 'w', encoding='gbk', newline='') as csv_file:
        writer = csv.writer(csv_file)
        column = ['时间', '气温', '风向', '湿度', '降雨概率']
        writer.writerow(column)
        i = 1
        for it in hourly_data['hourly']:
            dict = {}
            dict['时间'] = i
            dict['气温'] = it['temp']
            dict['风向'] = it['windDir']
            dict['湿度'] = it['humidity']
            dict['降雨概率'] = it['pop']
            writer.writerow(dict[col] for col in column)
            i += 1

