list1=[1, -3, -2, 6, 84, 34, -134, 57, 2, -5671, 8, 47, -0.5, 2.7, -11,  177, 88, 6, 2, 0.5]
x=10
y=4
positive_numbers=[]
greater_than_x=[]
for i in list1:
    if i>x:
        greater_than_x.append(i)
print(f"1. Числа, більші за х: {greater_than_x}") 

for i in list1:
    if i>0:
        positive_numbers.append(i)  #цей список використається і для середнього додатніх, і для 6 пункту(витяг додатних чисел)
print(f"2. Середнє додатних чисел: {round(sum(positive_numbers)/len(positive_numbers), 3)}")

less_than_x=[]
for i in list1:
    if i<x:
        less_than_x.append(i)
print(f"3. Найбільше число, що менше за х: {max(less_than_x)}")

sum_4=0
for i in list1:
    if i%4==0:
        sum_4+=i
print(f"4. Сума чисел, що діляться на 4:{sum_4}")

list_of_squares=[]
for i in list1:
    list_of_squares.append(i**2)

print(f"5. Квадрати елементів: {list_of_squares}")

print(f"6. Додатні елементи: {positive_numbers}")

list2=["Відійшла", "Підійшла", "Відрізала", "Від'їхала", "Ваніль"]
list21=[]
for i in list2:
    if i.startswith("Від"): 
        list21.append(i)
print(f"7. Слова, що починаються з префіксу 'від': {list21}")

n=3
sum_8=0
for i in range(3):
    sum_8+=list1[i]
print(f"8. Сума перших n елементів:{sum_8}")

list3=["око", "кіт", "солодощі", "Кит на морі романтик", "вирив", "Пилип"]
list31=[]
list32=[]
for i in list3:
    i=i.lower()
    i=i.replace(" ", "")
    list31.append(i)
for j, i in enumerate(list31):
    another_way=i[::-1]
    if another_way==i:
        list32.append(list3[j])
print(f"9. Паліндроми:{list32}")

#10. Перевірка подільності: зі списку чисел створіть новий список логічних значень, де кожен елемент вказує, 
# чи ділиться відповідне число на даний дільник
divider=3
list4=[3, 1, -6, 5, 365, 243, 9876, 153, 71445, 2881, 1644]
list_of_booleans=[]
for i in list4:
    if i%divider==0:
        list_of_booleans.append(True)
    else:
        list_of_booleans.append(False)
print(f"10. Чи ділиться на число: {list_of_booleans}")