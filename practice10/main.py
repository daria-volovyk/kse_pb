import json
from data.data import get_data, load_data

def create_hall(file_path):
    halls=get_data(file_path)
    new_hall=int(input("Введіть номер залу"))
    if new_hall in halls:
        print("Цей зал уже існує")
    else:
        num_rows=int(input("Number of rows"))
        num_columns=int(input("Number of columns"))
        new_hall_dict={new_hall:[]}
        for i in range(1, num_rows+1):
            for j in range(1, num_columns+1):
                seat_dict={f"{i}-{j}": False}
                new_hall_dict[new_hall].append(seat_dict)
        halls.update(new_hall_dict)
    load_data(halls, file_path)

file_path="data/cinema_halls.json"

def show_empty_seats(file_path):
    halls=get_data(file_path)
    hall_name=input("Введіть номер залу")
    if hall_name not in halls:
        print("Hall doesnt exist")
    else:
        selected_hall=halls[hall_name]
        empty_seats=[]
        seats=selected_hall.values()
        for seat in selected_hall:
            for key, value in seat.items():
                if value is False:
                    empty_seats.append(key)
                print(empty_seats)
show_empty_seats(file_path)
'''
while True:
    choice=int(input("Введіть дію"))
    if choice==0:
        break
    elif choice==1:
        print("add_hall")
        create_hall(file_path)
        pass
    elif choice==2:
        print("show empty seats")
        pass
    elif choice==3:
        print("book the seat")
        pass
    elif choice==4:
        print("Decline reserve")
        pass
'''
