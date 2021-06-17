import time
from datetime import datetime

def open():    #问问题
    name1 =input("你叫什么名字？")
    age1 = int(input("你几岁了？"))
    if(age1 <= 20):
        print("你真年轻。")
    elif(age1 <= 40):
        print(f"愿{age1}岁的你事业有成")
    else:
        print("您好。")
    print("\n命令指南：\nhello：问好\ntime：时间\nweather：实时天气\n88：退出程序\n我也可以陪你摸摸鱼")

    return name1

def welcome(name,robot):    #问好
    print(f"你好，我是机器人{robot}。")
    print(f"很高兴见到你，{name}同学")
    print("愿我们未来相处愉快。")

def show_time():   #时间
    dt=datetime.now()  #时间-现在时间：[变量名]=datetiame.now()
    print(f"现在是北京时间：{dt.year}年{dt.month}月{dt.day}日 {dt.hour}时{dt.minute}分{dt.second}秒")  #第一种
    print(dt.strftime("It is %Y-%m-%d  %H:%M:%S now.")) #第二种  Python3.8中[变量名].strftime()无法加入中文，会报错。

def run_nian(year):     #闰年
    return year %4==0 and year %100!=0 or year %400==0

def run_1(year):    #Ex_bool_闰年.py
    if(year %4 == 0 and year %100 !=0 or year %400 == 0):
        print(f"{year}年是闰年。")
    else:
        print("我想想...")
        time.sleep(2)
        print(f"{year}年不是闰年")

assert run_nian(2000) == True
assert run_nian(2100) == False 
assert run_nian(2020) == True  #assert 断言：判断函数输出是否为要求内容。同样执行assert的函数中的所有命令，如print()等。

def replacement(question):  #划水（字符替换）
    return question.replace("你","我").replace("不","").replace("吗","").replace("？","！").replace("?","!")

def tianqi(city):   #天气
        url ="https://devapi.qweather.com/v7/weather/now?location=101020200&key=e43d4a9cee1c4b7b98edfeca3d77f40d"
        import requests
        res = requests.get(url)
        tq_text= res.text
        import json
        tq_json= json.loads(tq_text)
        temperature= tq_json["now"]["temp"]
        weather_now= tq_json["now"]["text"]
        windDir= tq_json["now"]["windDir"]
        windScale =tq_json["now"]["windScale"]
        humidity =tq_json["now"]["humidity"]
        print(f"{city}实时天气：\n天气：{weather_now}\n温度：{temperature}℃\n风向：{windDir}\n湿度：{humidity}%")