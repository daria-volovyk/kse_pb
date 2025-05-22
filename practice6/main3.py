import taxes
amount=15000
a=taxes.calculate_vat(amount)
b=taxes.calculate_income_tax(amount+a)
print(a)
print(b)
print(a+b)