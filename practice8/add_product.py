def add_product(inventory, name, quantity):
    if(name in inventory):
        inventory[name]["quantity"]+=quantity
    else:
        d=int(input("Введіть ціну товару"))
        inventory[name]={"price":d, "quantity":quantity}
    return inventory
