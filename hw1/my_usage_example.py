from my_transaction_manager import TransactionManager

def buy_ticket(cursor):
    query = "INSERT INTO fly_booking (client_name, fly_number, from_place, to_place, booking_date) VALUES (%s, %s, %s, %s, NOW());"
    data = ("Roman Vey", "NUMB 1", "UKR", "NOR")
    cursor.execute(query, data)


def order_hotel(cursor):
    query = "INSERT INTO hotel_booking (client_name, hotel_name, arrival, departure) VALUES (%s, %s, NOW(), NOW());"
    data = ("Roman Vey", "Nice Hotel")
    cursor.execute(query, data)


def add_account(cursor):
    query = "INSERT INTO account (client_name, amount) VALUES (%s, %s);"
    data = ("Roman Vey", "1000")
    cursor.execute(query, data)


def decrease_money(cursor, money):
    query = "UPDATE account SET amount = amount - %s WHERE client_name = 'Roman Vey';"
    data = (money, )
    cursor.execute(query, data)

def get_transaction_status(cursor):
    pass

def delete_account(cursor):
    query = "DELETE FROM account"
    cursor.execute(query)

def delete_fly_booking(cursor):
    query = "DELETE FROM fly_booking"
    cursor.execute(query)

def delete_hotel_booking(cursor):
    query = "DELETE FROM hotel_booking"
    cursor.execute(query)


tm = TransactionManager(user="postgres", password="postgres", host="localhost", port="5432", verbose=False)
tm.add_connection("fly_booking", database="fly_booking_db")
tm.add_connection("hotel_booking", database="hotel_booking_db")
tm.add_connection("account", database="account_db")


tm.add_to_transaction("create_me", "account", add_account, comment="Create my account with $1000")
tm.add_to_transaction("delete_me", "account", delete_account, comment="Delete all accounts")
tm.add_to_transaction("delete_hotel_booking", "hotel_booking", delete_hotel_booking, comment="Delete all hotel bookings")
tm.add_to_transaction("delete_fly_booking", "fly_booking", delete_fly_booking, comment="Delete all fly bookings")



tm.add_to_transaction("book_hotel", "account", delete_account, comment="Delete all accounts")
tm.add_to_transaction("book_hotel", "hotel_booking", order_hotel, comment="Book 200$ hotel")
tm.add_to_transaction("book_hotel", "account", decrease_money, [200], comment="Remove 200$ from account")

tm.add_to_transaction("book_all", "hotel_booking", order_hotel, comment="Book 200$ hotel")
tm.add_to_transaction("book_all", "account", decrease_money, [200], comment="Remove 200$ from account")
tm.add_to_transaction("book_all", "fly_booking", buy_ticket, comment="Buy 300$ flight ticket")
tm.add_to_transaction("book_all", "account", decrease_money, [300], comment="Remove 300$ from account")



def run_scanario_success():
    print("-" * 20)
    print("Run success scenario:")
    print("-" * 20)
    tm.run_transaction("delete_me")
    tm.run_transaction("delete_hotel_booking")
    tm.run_transaction("delete_fly_booking")
    tm.run_transaction("create_me")
    for _ in range(2):
        tm.run_transaction("book_all")


def run_scanario_failed():
    print("-" * 20)
    print("Run failed scenario:")
    print("-" * 20)
    tm.run_transaction("delete_me")
    tm.run_transaction("delete_hotel_booking")
    tm.run_transaction("delete_fly_booking")
    tm.run_transaction("create_me")
    for _ in range(3):
        tm.run_transaction("book_all")

    

if __name__ == "__main__":
    tm.run_transaction("create_me")
    #run_scanario_failed()
    #run_scanario_success()