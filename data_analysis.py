import math
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def tem_curve_day(data):
    """温度曲线绘制"""
    date = list(data['时间'])
    tem = list(data['气温'])
    tem_ave = sum(tem) / len(tem)  # 求平均温度
    plt.plot([1, len(tem)], [tem_ave, tem_ave], c='red', linestyle='--')  # 画出平均温度虚线
    tem_max = max(tem)
    tem_max_date = tem.index(tem_max)  # 求最高温度
    tem_min = min(tem)
    tem_min_date = tem.index(tem_min)  # 求最低温度
    x = []
    y = []
    for i in range(0, 24):
        x.append(i)
        y.append(tem[i])
    plt.figure(1)
    plt.plot(x, y, color='red', label='温度')  # 画出温度曲线
    plt.scatter(x, y, color='red')  # 点出每个时刻的温度点
    plt.plot([0, 24], [tem_ave, tem_ave], c='blue', linestyle='--', label='平均温度')  # 画出平均温度虚线
    plt.text(tem_max_date + 0.15, tem_max + 0.15, str(tem_max), ha='center', va='bottom', fontsize=10.5)  # 标出最高温度
    plt.text(tem_min_date + 0.15, tem_min + 0.15, str(tem_min), ha='center', va='bottom', fontsize=10.5)  # 标出最低温度
    plt.xticks(x)
    plt.legend()
    plt.title('未来24小时气温预测曲线图')
    plt.xlabel('时间/h')
    plt.ylabel('摄氏度/℃')
    plt.savefig('./png/tem_24h.png')
    plt.show()

def rain_curve(data):
    """降雨概率柱状图"""
    date = list(data['时间'])
    rain = list(data['降雨概率'])
    rain_ave = sum(rain) / len(rain)  # 求平均降雨概率
    plt.figure(2)
    plt.bar(date, rain, color='blue', label='降雨概率')  # 画出降雨概率柱状图
    plt.plot([0, 24], [rain_ave, rain_ave], c='red', linestyle='--', label='平均降雨概率')  # 画出平均降雨概率虚线
    plt.text(0.5, rain_ave + 0.15, str(rain_ave), ha='center', va='bottom', fontsize=10.5)  # 标出平均降雨概率
    plt.legend()
    plt.title('未来24小时降雨概率柱状图')
    plt.xlabel('时间/h')
    plt.ylabel('降雨概率/%')
    plt.savefig('./png/rain_24h.png')
    plt.show()


def hum_curve(data):
    """相对湿度曲线绘制"""
    hour = list(data['时间'])
    hum = list(data['湿度'])
    hum_ave = sum(hum) / 24  # 求平均相对湿度
    hum_max = max(hum)
    hum_max_hour = hour[hum.index(hum_max)]  # 求最高相对湿度
    hum_min = min(hum)
    hum_min_hour = hour[hum.index(hum_min)]  # 求最低相对湿度
    x = []
    y = []
    for i in range(1, 25):
        x.append(i)
        y.append(hum[hour.index(i)])
    plt.figure(2)
    plt.plot(x, y, color='blue', label='相对湿度')  # 画出相对湿度曲线
    plt.scatter(x, y, color='blue')  # 点出每个时刻的相对湿度
    plt.plot([0, 24], [hum_ave, hum_ave], c='red', linestyle='--', label='平均相对湿度')  # 画出平均相对湿度虚线
    plt.text(hum_max_hour + 0.15, hum_max + 0.15, str(hum_max), ha='center', va='bottom', fontsize=10.5)  # 标出最高相对湿度
    plt.text(hum_min_hour + 0.15, hum_min + 0.15, str(hum_min), ha='center', va='bottom', fontsize=10.5)  # 标出最低相对湿度
    plt.xticks(x)
    plt.legend()
    plt.title('一天相对湿度变化曲线图')
    plt.xlabel('时间/h')
    plt.ylabel('百分比/%')
    plt.savefig('./png/hum_24h.png')
    plt.show()


def analysis():
    """24h曲线绘制"""
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 解决中文显示问题
    plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题
    data = pd.read_csv('weather.csv', encoding='gbk')
    tem_curve_day(data)
    rain_curve(data)
    hum_curve(data)


