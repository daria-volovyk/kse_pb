import datetime
birth=input("Введіть дату народження (рррр-мм-дд):")
t=datetime.datetime.today()
bd=datetime.datetime.strptime(birth, "%Y-%m-%d")
result=(t-bd).days
print( f"прожито {result} днів")