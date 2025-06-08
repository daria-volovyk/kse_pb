x=2
y=4
list1=[2, 4, 1, 6, 10, 12, 15, 17, 20, 22, 30, 27]
list1_1=[]
for i in list1:
    if i%2==0 and i%4!=0:
        list1_1.append(i)
print(f"1. Числа, що діляться на х, але не діляться на у: {list1_1}")

list2=[[1, 3, 4], [35, 45, 1], ["собака", "з'їла", "коврик"]]
list2_1=[]
for i in list2:
    for j in i:
        list2_1.append(j)
print(f"2. Один список: {list2_1}")

text1="Треба те, треба се, але нікому не цікаво, що треба мені!!"
text1=text1.lower()
list3=text1.split(" ")
for j, i in enumerate(list3):
    if i=="треба":
        list3[j]=list3[j].upper()
print(f"3. {" ".join(list3)}")

list4=[5, 7, 887, 66, 2, 1, 3, 66, 1, 4, 7, 25, 8, 7, 7, 8]
dict4={}
dict4_1={}
for i in list4:
    if i in dict4.keys():
            dict4[i]+=1
    else: 
        dict4[i]=1
for key, value in dict4.items():
    dict4_1=dict(sorted(dict4.items(), key=lambda item:(item[1], item[0]), reverse=True)) #використано гугл
l4=list(dict4_1.keys())
print(f"4. Багаторівневе сортування: {l4}")


list5_1=[4, 4, 78, 2, 88, 33, 45, 'veer']
list5_2=['ffd', 'rt', 'wfwe', 8, 5324, 9, 14, 88]
list5_3=[]
for j, i in enumerate(list5_1):
    if (type(list5_1[j])==int or type(list5_1[j])==float) and (type(list5_2[j])==int or type(list5_2[j])==float):
        list5_3.append(list5_1[j]-list5_2[j])
    else: list5_3.append((str(list5_1[j])+str(list5_2[j])))
print(f"5. Об'єднання рядків: {list5_3}")

list6=[{1: 3424, 2:463, 3:63, 5:74, 123: 54, 7: 421}, {3:52, 22:543, 7:321, 220:32, 1:44}]
quantity6=[]
dict6={}
for i in list6:
    for key, value in i.items():
        if key in dict6.keys():
            dict6[key]+=value
        else: 
            dict6[key]=value

print(f"6. Оновлений словник: {dict6}")

list7=[1, 5, 'dv', 6, 'gfwe', 8, 234, 'dvsfe']
list7_1=[]
for  i in list7:
    if type(i)==str:
        list7_1.append("користувачем введено неправильне значення")
    else:
        list7_1.append(i)
print(f"7. Новий список: {list7_1}")



x2=4
quantity=0
text8=["слово", "ліжко", "рука", "ідентифікація", "око", "ніс", "абсорбація", "холодильник"]
lenth_of_strings=[]
for i in text8:
    lenth_of_strings.append(len(i))
for j, i in enumerate(text8):
    if lenth_of_strings[j]>x2:
        quantity+=1
print(f"8. Кількість рядків, у яких більше ніж х символів: {quantity}")

list9_1=[5, 8, 3, 1]
list9_2=['gr', 'fdc', 'dfss', 'fsvs']
list9_3=[]
for i, j in enumerate(list9_1):
    list9_3.append(str(list9_1[i])+str(list9_2[i]))
print(f"9. Почергове об'єднання:{list9_3}")

x=10
y=3
list10=[3, 154, 5.6, 86, 112.5, 7]
list10_1=[]
for i in list10:
    if i>x:
        list10_1.append(i*y)
    else:
        list10_1.append(i)
print(f"10. {list10_1}")