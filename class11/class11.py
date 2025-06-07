# 複製 list, 避免原本的 List 被更動
L = ["hello", "world"]
L2 = L.copy()  # 使用 copy() 複製 List
print(L2)  # ['hello', 'world']
L2[0] = "python"  # 修改 L2
print(L2)  # ['python', 'world'] # 修改 L2 不會影響 L
print(L)  # ['hello', 'world'] # 原本的 L 不受影響
# 這跟變數的=賦值不同 ,一般情況下會開2個記憶體空間 ,
# 在List的情況下,只會開一個記憶體空間
# 這導致原本的 List 被更動
# 如果想要取得原本的 List 可以使用 L.copy()

# remove : 移除 List 中指定的元素(只會移除第一個找到的)
L = ["Hello", "World", "Python"]
L.remove("World")  # 移除 World
print(L)  # ['Hello', 'Python']

# pop : 刪除 List 中最後一個元素
L = ["Hello", "World", "Python"]
# 不給索引時 ,pop() 會刪除最後一個元素
L.pop()  # 移除最後一個元素
print(L)  # ['Hello', 'World']
s = L.pop(1)  # 移除索引 1 的元素 , 並回傳該值
print(s)  # World
print(L)  # ['Hello']

print("購物清單:")
print("目前清單是空的")
L = ["新增東西", "修改東西", "刪除東西", "離開程式"]
L2 = []
while True:
    print(f"目前清單是{L2}")
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
            i = int(input("請輸入插入位置:"))
            L2.insert(i, d)
            print(f"新增東西{d}")
    elif f == 2:
        z = int(input("請輸入你要修改的東西的編號:"))
        d = input("請輸入要修改的東西:")
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
