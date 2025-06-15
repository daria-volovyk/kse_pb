def add_transaction(transactions, amount, transaction_type, category):
    for amount in transactions:
        if transaction_type=="дохід":
            pass
        elif transaction_type=="витрата":
            pass

transactions = []
add_transaction(transactions, 10000, "дохід", "зарплата")
add_transaction(transactions, 2500, "витрата", "їжа")
add_transaction(transactions, 1500, "витрата", "транспорт")
