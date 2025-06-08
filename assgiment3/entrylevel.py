list1=[1, 6, 84, 34, 57, 2, 8, 47, 2.7, 177, 88, 6, 2, 0.5]
sum1=sum(list1)
min1=min(list1)
num=5
print(f"1: Сума елементів списку: {sum1}")
print(f"2: Найменший елемент: {min1}")
print(f"3: Перевернутий список: {list1[::-1]}")
list2=[]
for i in list1:
    if i%2!=0 and i.is_integer():
        list2.append(i)
print(f"4: Непарні числа: {list2}")
list3=[]
for i in list1:
    list3.append(i*num)
print(f"5: Список помножений на число num:{list3}")
    