import random

# 猜数字    
targetValue = random.randint(0, 999)
while True:
    inputStr = input("请输入一个3位以内的数，猜答案:")
    inputValue = "输入的数据"
    try:
        inputValue = int(inputStr)
    except ValueError as e:
        print("只允许输入数字")
        continue

    if inputValue > 1000:
        print("只允许输入3位数的数字")
        continue
    
    if inputValue == targetValue:
        print("你猜对了！！！！！！！")
        break
    elif inputValue > targetValue:
        print("猜得有点大")
    else:
        print("猜得有点小")
     