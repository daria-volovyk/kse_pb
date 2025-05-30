from data import inventory
import add_product
import buy_product
while True:
    action=int(input("Введіть дію"))
    if(action==1):
        name=input("Введіть товару")
        quantity=input("Введіть кількість")
        inventory = add_product(inventory, name, quantity)
    if(action==2):
        quantity=input("Введіть кількість")
        buy_product(inventory, name, quantity)
    if(action==3):
        print(inventory)
    if(action==0):
        break
    