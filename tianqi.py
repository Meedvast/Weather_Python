from xpinyin import Pinyin
import requests
import re
import csv


def write_csv():
    p = Pinyin()
    ret = gui.text_city.get()
    city = re.sub(r'[-]', "", ret)
    dict = {}  # 空字典

    time = '202206'
    domain = "https://lishi.tianqi.com/" + city + "/" + time + ".html"
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
    }
    obj1 = re.compile(r'<ul class="thrui">(?P<weather>.*?)<div class="lishidesc2">', re.S)
    obj2 = re.compile(r'<div class="th...">(?P<infor>.*?)</div>', re.S)
    resp = requests.get(domain, headers=header)
    resp.encoding = 'utf-8'
    result1 = obj1.search(resp.text)
    result2 = obj2.finditer(result1.group("weather"))
    i = 0
    with open('tianqi.csv', 'w', encoding='gbk', newline='') as csv_file:
        writer = csv.writer(csv_file)
        column = ['日期', '最高气温', '最低气温', '天气', '风向风级', ' ']
        writer.writerow(column)
        for it in result2:
            if i % 6 == 0:
                dict['日期'] = it.group("infor").split(" ")[0]
                i = 0
            if i % 6 == 1:
                dict['最高气温'] = int(it.group('infor').replace('℃', ''))
            if i % 6 == 2:
                dict['最低气温'] = int(it.group('infor').replace('℃', ''))
            if i % 6 == 3:
                dict['天气'] = it.group('infor')
            if i % 6 == 4:
                dict['风向风级'] = it.group('infor')
            if i % 6 == 5:
                dict[' '] = it.group('infor')
                writer.writerow(dict[col] for col in column)
            i += 1
