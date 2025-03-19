"""
請問Python有哪四種形態:
答案:
整數、小數、布林、字串
請問使用什麼指令可以顯示出形態
答案:
type()
請問今天學了哪一些指令(函式)?
答案:
print、input、type、int、float、str、bool、max、len
延續上題, 請嘗試描述每個指令的功能各別是什麼?
答案:

print：用於顯示輸出到控制台。
input：用於從使用者獲取輸入。
type：用於顯示變數的資料類型。
int：用於將資料轉換為整數型態。
float：用於將資料轉換為浮點數型態。
str：用於將資料轉換為字串型態。
bool：用於將資料轉換為布林型態。
max：用於獲取一組數字中的最大值。
len：用於獲取字串或列表的長度。
"""

"""
請使用者輸入身高(公尺)h以及體重(公斤)w
透過下面公式計算出BMI數值並顯示計算結果
bmi = w/h**2
EX:
請輸入身高:1.7
請輸入體重:50
你的BMI為17.301038062283737
"""
h = float(input("請輸入身高: "))
w = float(input("請輸入體重: "))
bmi = w / h**2
print(f"你的BMI為: {bmi}")
