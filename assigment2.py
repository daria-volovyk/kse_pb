print("Завдання 1")
text="Hello, Python World!"
print(text)
print()

print("Завдання 2")
num1=float(input("Введіть перше число"))
num2=float(input("Введіть друге число"))
print(f"Результат додавання:{num1}+{num2}={num1+num2}")
print(f"Результат віднімання:{num1}-{num2}={num1-num2}")
print(f"Результат множення:{num1}*{num2}={num1*num2}")
print(f"Результат ділення:{num1}/{num2}={num1/num2}")
print()

print("Завдання 3")
str1="це є"
str2=" третє завдання"
print(str1+str2)
print(f"Довжина рядка: {len(str1+str2)}")
print()

print("Завдання 4")
odd_or_even=int(input("Введіть число на перевірку парності"))
if(odd_or_even%2==0):
    print("Парне")
else:
    print("Непарне")
print()

print("Завдання 5")
for i in range(1, 11):
    print(i)
print()

print("Завдання 6")
num=float(input("Введіть число на перевірку знаку"))
if(num>0):
    print("Позитивний")
elif(num<0):
    print("Негативний")
else:
    print("Нуль")
print()

print("Завдання 7")
for i in range(2, 11, 2):
    print(i)
print()

print("Завдання 8")
n=int(input("Введіть число"))
i=1
sum=0
while i!=n+1: #якщо включно n
    sum+=i
    i+=1
print(sum)
print()

print("Завдання 9")
i=10
while i!=0:
    print(i)
    i-=1
print()

print("Завдання 10")
for i in range(1, 11):
    if(i==5):
        continue
    if(i==7):
        break
    print(i)
