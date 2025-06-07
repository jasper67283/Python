print("購物清單:")
print("目前清單是空的")
L = ["新增東西", "修改東西", "刪除東西", "離開程式"]
L2 = []
while True:
    print(f"目前清單是{L}")
    print("功能選單:")
    print(f"1.{L[0]}")
    print(f"2.{L[1]}")
    print(f"3.{L[2]}")
    print(f"4.{L[3]}")
    f = int(input("請輸入你的選擇(1~4):"))

    if f == 1:
        print("a. 加到尾端")
        print("b. 插入指定位置")
        d = input("請輸入新增的東西:")
        s = input("請選擇方法(a/b):")
        if s == "a":
            L2.append(d)
            print(f"新增東西{d}")
        elif s == "b":
            print("請輸入插入位置:")
            i = int(input("請輸入數字:"))
            L2.insert(i, d)
            print(f"新增東西{d}")
    elif f == 2:
        z = int(input("請輸入你要修改的東西的編號:"))
        d = input("請輸入新增的東西:")
        L2[z] = d
        print(f"修改東西{d}")
    elif f == 3:
        print(f"a. 依名稱刪除 b. 依位置刪除")
        s = input("請選擇方法(a/b):")
        if s == "a":
            print("請輸入你要刪除的東西的名稱:")
            d = input("請輸入東西名稱:")
            L2.remove(d)
            print(f"刪除東西{d}")
        elif s == "b":
            print("請輸入你要刪除的東西的位置(從零開始):")
            i = int(input("請輸入數字:"))
            L2.pop(i)
            print(f"刪除東西{i}")
    elif f == 4:
        print("再見!")
        break
    else:
        break
