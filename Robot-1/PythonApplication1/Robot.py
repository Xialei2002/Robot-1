import module1_open as mod1 

robotname= "AP-1"
name=mod1.open()        #1.问问题

#4.对话
while(True):
    print("-------------------------")
    print("您有什么吩咐？")
    command=input()
    if(command == "time"):
        mod1.show_time()                                   #3.显示时间
    elif(command == "hello"):
        mod1.welcome(name,robotname)                       #2.问好
    elif(command == "weather"):
        mod1.tianqi("闵行")                                #7.实时天气
    elif(command == "88"):
        print(f"{robotname}：88，{name}，下次再见！")      #6.退出循环
        break 
    else:
        print(mod1.replacement(command))                   #5.回答（浑水摸鱼）
