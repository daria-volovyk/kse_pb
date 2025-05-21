#Є вкладений список оцінок студентів. Кожен підсписок — це список оцінок одного студента.
#Виведіть індекс студента з найвищим середнім балом, його середній бал та сам список оцінок
grades = [
    [90, 85, 88],
    [75, 80, 79],
    [95, 92, 96],
    [88, 85, 84]
]
means=[]
for i in grades:
  means.append(sum(i)/len(i))
print(means)
mv = max(means)
print(mv)
for i, means1 in enumerate(means):
  if(means1==mv):
    print(i)
print(grades[2])