#Є словник, де ключі — назви товарів, а значення — їхня ціна. 
#Обчисліть загальну суму вартості всіх товарів.
prices = {
    "apple": 12,
    "banana": 8,
    "milk": 25,
    "bread": 20
}
m= list(prices.values())
summa=0
print(m)
for i in m:
  summa+=i
print(summa)