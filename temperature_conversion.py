# 這是一個簡單的溫度轉換程式
c = input('請輸入攝氏溫度:')
c = float(c)
f = c * (9 / 5) + 32
k = 273.15 + c
print('華氏溫度為:', f, '克氏溫度為:', k)