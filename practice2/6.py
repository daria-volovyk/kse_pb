height=float(input("Введіть зріст у сантиметрах"))
weight=float(input("Введіть вагу в кілограмах"))
bmi=weight**2/height
#print("При вазі " + str(weight) + " та рості " + str(height)+ " Ваш ВМІ складає " + str(bmi))
print(f"При вазі {weight} та рості {height} Ваш ВМІ складає {bmi}")