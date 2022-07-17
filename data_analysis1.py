from matplotlib import pyplot as plt
import pandas as pd


def tem_curve_month(data):
    """温度曲线绘制"""
    date = list(data['日期'])
    tem_low = list(data['最低气温'])
    tem_high = list(data['最高气温'])

    tem_high_ave = sum(tem_high) / len(tem_high)  # 求平均高温
    tem_low_ave = sum(tem_low) / len(tem_low)  # 求平均低温
    plt.plot([1, len(tem_high)], [tem_high_ave, tem_high_ave], c='black', linestyle='--')  # 画出平均温度虚线
    plt.plot([1, len(tem_low)], [tem_low_ave, tem_low_ave], c='black', linestyle='--')  # 画出平均温度虚线
    tem_max = max(tem_high)
    tem_max_date = tem_high.index(tem_max)  # 求最高温度
    tem_min = min(tem_low)
    tem_min_date = tem_low.index(tem_min)  # 求最低温度

    x = range(1, len(tem_high) + 1)
    plt.figure(1)
    plt.plot(x, tem_high, color='red', label='高温')  # 画出高温度曲线
    plt.scatter(x, tem_high, color='red')  # 点出每个时刻的温度点
    plt.plot(x, tem_low, color='blue', label='低温')  # 画出低温度曲线
    plt.scatter(x, tem_low, color='blue')  # 点出每个时刻的温度点

    plt.legend()
    plt.text(tem_max_date + 0.15, tem_max + 0.15, str(tem_max), ha='center', va='bottom', fontsize=10.5)  # 标出最高温度
    plt.text(tem_min_date + 0.15, tem_min + 0.15, str(tem_min), ha='center', va='bottom', fontsize=10.5)  # 标出最低温度
    plt.xticks(x)  # 设置x轴标签
    plt.title('查询月数30天高温低温变化曲线图')
    plt.xlabel('日期/天')
    plt.ylabel('摄氏度/℃')
    plt.savefig('./png/tem_month.png')
    plt.show()


def analysis_():
    """24h曲线绘制"""
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 解决中文显示问题
    plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题
    data = pd.read_csv('tianqi.csv', encoding='gbk')
    tem_curve_month(data)
