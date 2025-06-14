# index :尋找指定元素在 List 中第一次出現的位置
# 如果元素不存在會產生錯誤,所以使用前建議先檢查元素是否存在
L = [1, 2, 3, 4, 5]
print(L.index(3))  # 找到數字 3 在索引位置 1

# count : 統計某個元素在 List 中出現的次數
# 這個方法很適合用來檢查重複資料的數量
L = ["Hello", "World", "Python", "Hello"]
print(L.count("Hello"))  # "Hello" 這個字串在 List 中出現了 2 次

# sort : 將 List 中的元素進行排序, 預設是按照小到大(升序排列)
# 注意: 這個方法會直接修改原本的 List 資料,不會產生新的 List會產生新的 List
L = [1, 2, 3, 4, 5]
L.sort()
print(L)

# sort(reverse=True) : 將 List 中的元素由大到小排序(降序排列)
# reverse=True 可以將列表倒序
L = [1, 2, 3, 4, 5]
L.sort(reverse=True)
print(L)

# reverse : 將 List 中元素的順序反轉
# 這不是排序方法,只是將列表元素的順序反轉
L = [1, 2, 3, 4, 5]
L.reverse()
print(L)

# List 和字串有很多相似的操作方式
# 我們可以像操作字串一樣處理 List

# 合併兩個 List : 使用 +使用 + 運算子將兩個 List 合併
# 這個方法會產生一個新的 List , 不會直接修改原本的 List
L1 = [1, 2, 3]
L2 = [4, 5, 6]
L3 = L1 + L2  # 把 L1 和 L2 合併成一個 List
print(L3)

# 重複 List 中的內容 : 使用 * 運算子將兩個 List 重複
# 這在需要建立重複資料時很有用
L = [1, 2, 3]
L = L * 3  # 讓 List 的內容重複 3 次
print(L)

# 不同資料型態之間的轉換技巧
print(range(10))  # range 物件本身看不到具體內容,只是一個範圍描述
print(list(range(10)))  # 使用 list() 將 range 轉換成可看到內容的 list 物件
print(list("Hello"))  # 將字串轉換成 list 物件 , 每個字元就是一個元素

# split : 將一個完整的字串按照指定的分隔符號切割成多個部分
# 這是處理文字資料時常用的方法
s = "Hello World"
L = s.split(" ")  # 以空白字元作為分隔點來切割字串
print(L)
calendar = "2020-01-01"
L = calendar.split("/")  # 以 / 字元作為分隔點來切割字串
print(L)

# join : 將 List 中的元素進行合併,將元素組合成一個字串
# 可以指定要用什麼符號來連接元素
L = ["Hello", "World"]
s = " ".join(L)  # 以空白字元將 List 中的元素來連接字串
print(s)
