import tkinter
from tkinter import *
from PIL import ImageTk
from tkcalendar import Calendar
from PIL import Image
import data_analysis
import data_analysis1
import tianqi
import weather
import glo


def future():
    glo.text1 = text_city.get()
    weather.write_csv()  # 将未来24H天气数据写入csv文件
    data_analysis.analysis()
    img_open1 = Image.open('png/tem_24h.png')
    img_png1 = ImageTk.PhotoImage(img_open1)
    label_img1 = Label(root, image=img_png1)
    label_img1.place(x=10, y=200, width=640, height=480)
    img_open2 = Image.open('png/hum_24h.png')
    img_png2 = ImageTk.PhotoImage(img_open2)
    label_img2 = Label(root, image=img_png2)
    label_img2.place(x=650, y=200, width=640, height=480)
    img_open3 = Image.open('png/rain_24h.png')
    img_png3 = ImageTk.PhotoImage(img_open3)
    label_img3 = Label(root, image=img_png3)
    label_img3.place(x=1290, y=200, width=640, height=480)
    root.mainloop()


def past():
    img_open1 = Image.open('png/tem_month.png')
    img_png1 = ImageTk.PhotoImage(img_open1)
    label_img1 = Label(root, image=img_png1)
    label_img1.place(x=10, y=200, width=640, height=480)
    label_img2 = Label(root)
    label_img2.place(x=650, y=200, width=640, height=480)
    label_img3 = Label(root)
    label_img3.place(x=1290, y=200, width=640, height=480)
    root.mainloop()


root = Tk()
root.title("天气预报")
root_width = 800
root_height = 400
root_width_x = (root.winfo_screenwidth() - root_width) / 2
root_height_y = (root.winfo_screenheight() - root_height) / 2
root.geometry("%dx%d+%d+%d" % (root_width, root_height, root_width_x, root_height_y))

label_city = Label(width=10, text="请输入城市")
label_city.place(x=10, y=10)
text_city = Entry(width=10)
text_city.place(x=100, y=10)

btn_past = Button(width=15, text="查询历史天气", command=past)
btn_past.place(x=10, y=50)

btn_future = Button(width=20, text="显示未来24小时天气预报", command=future)
btn_future.place(x=10, y=100)


label_img1 = Label(root)
label_img2 = Label(root)
label_img3 = Label(root)

root.mainloop()
