import main.py
transactions=[]
def buy_product(inventory, transactions, name, quantity, seller_id):
    if(inventory[name]["quantity"]>0):
        inventory[name]["quantity"]-=quantity
        transactions.append()
    else:
        return ("Товару немає")
    return quantity*main.price

