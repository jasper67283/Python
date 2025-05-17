# append 加入到列表的最後一筆資料
L = ["hello", "world"]
L.append("python")  # 加入python
print(L)  # ['hello', 'world', 'python']

# insert 加入到列表的指定位置
L = ["hello", "world"]
L.insert(1, "python")  # 加入python
print(L)  # ['hello', 'python', 'world']

# 修改列表的指定位置
L = ["hello", "world"]
L[1] = "python"  # 修改python
print(L)  # ['hello', 'python']

L = ["1", "2", "3", "4", "5", "6", "7"]
print(L)
while True:
    try:
        f = int(input("請輸入數字(1~7):"))
    except:
        print("請輸入有效的數字")
    else:
        if f > len(L) or f < 1:
            print("輸入錯誤查無此數字 請重新輸入")
        else:
            print("您想要修改的數字是" + str(f))
            print("原本的天氣是" + L[f - 1])
            s = input("請輸入數字:")
            L[f - 1] = s
            print("修改後的天氣是" + L[f - 1])
            print(L)
            break
