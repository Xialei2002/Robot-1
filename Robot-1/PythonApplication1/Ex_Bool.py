#逻辑值的检测
#1.数字：0为False，其他为True
if(5):
    print(1)  #此处5==True

if(0):
    print(2)  #此处0=False，2不打印

#2.字符串：空的为False，其他为True

a =""
if(a):
    print(1) 

b="b"
if(b):
    print(2)

#None
if(None):
    print(1)

#列表，字典，元组：空的为False，其他为True
