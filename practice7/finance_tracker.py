def add_transaction(transactions, amount, transaction_type, category):
    for amount in transactions:
        if transaction_type=="дохід":
        if transaction_type=="витрата":

transactions = []
add_transaction(transactions, 10000, "дохід", "зарплата")
add_transaction(transactions, 2500, "витрата", "їжа")
add_transaction(transactions, 1500, "витрата", "транспорт")
