import datetime
import tkinter
from tkinter import *
from tkcalendar import Calendar
from PIL import Image, ImageTk
import data_analysis
import data_analysis1
import tianqi
import weather


def Start_calendar():
    def print_sel():
        text_time.configure(state="normal")
        s_data = cal.selection_get().strftime('%Y%m%d')
        text_time.delete(0, END)
        text_time.insert("0", s_data)
        text_time.configure(state="disabled")
        top.destroy()

    top = Toplevel()
    top.geometry("300x250")

    today = datetime.date.today()

    mindate = datetime.date(year=2011, month=1, day=1)
    maxdate = today + datetime.timedelta(days=14)

    cal = Calendar(top, font="Arial 14", selectmode='day', locale='zh_CN', mindate=mindate, maxdate=maxdate,
                   background="white", foreground="black", bordercolor="white", selectbackground="gray",
                   selectforeground="white", showweeknumbers=False, disabledselectbackground=False)
    cal.place(x=0, y=0, width=300, height=200)

    btn1 = Button(top)
    btn1["text"] = "确定"
    btn1["command"] = print_sel
    btn1.place(x=240, y=205)


def Future():
    weather.write_csv()  # 将未来24H天气数据写入csv文件
    data_analysis.analysis()
    show_image('png/tem_24h.png', 'png/hum_24h.png', 'png/rain_24h.png')


def Past():
    data_analysis1.analysis_()
    show_img('png/tem_month.png')


# 显示PNG图片
def show_image(path, path1, path2):
    global label_img, label_img1, label_img2
    img_open = Image.open(path)
    img_png = ImageTk.PhotoImage(img_open)
    label_img = tkinter.Label(root, image=img_png)
    label_img.place(x=10, y=300, width=640, height=480)
    img_open1 = Image.open(path1)
    img_png1 = ImageTk.PhotoImage(img_open1)
    label_img1 = tkinter.Label(root, image=img_png1)
    label_img1.place(x=650, y=300, width=640, height=480)
    img_open2 = Image.open(path2)
    img_png2 = ImageTk.PhotoImage(img_open2)
    label_img2 = tkinter.Label(root, image=img_png2)
    label_img2.place(x=1290, y=300, width=640, height=480)
    root.mainloop()


def show_img(path):
    global label_img3
    label_img.destroy()
    label_img1.destroy()
    label_img2.destroy()
    img_open = Image.open(path)
    img_png = ImageTk.PhotoImage(img_open)
    label_img3 = tkinter.Label(root, image=img_png)
    label_img.place(x=10, y=300, width=640, height=480)
    root.mainloop()


root = Tk()
root.title("天气预报")
root_width = 1980
root_height = 1080
root_width_x = (root.winfo_screenwidth() - root_width) / 2
root_height_y = (root.winfo_screenheight() - root_height) / 2
print(root_width)
root.geometry("%dx%d+%d+%d" % (root_width, root_height, root_width_x, root_height_y))

btn_time = Button(width=10, text="请输入时间", command=Start_calendar)
btn_time.place(x=10, y=10)
text_time = Entry(width=20)
text_time.place(x=100, y=10)

label_city = Label(width=10, text="请输入城市")
label_city.place(x=10, y=60)
text_city = Entry(width=10)
text_city.place(x=100, y=60)

btn_past = Button(width=15, text="查询历史天气", command=Past)
btn_past.place(x=10, y=100)

btn_future = Button(width=20, text="显示未来24小时天气预报", command=Future)
btn_future.place(x=10, y=150)

btn_quit = Button(width=10, text="退出", command=root.destroy)
btn_quit.place(x=280, y=140)

root.mainloop()
