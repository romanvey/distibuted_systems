import psycopg2
from transaction_manager import TransactionManager

tm = TransactionManager(user="postgres", password="postgres", host="localhost", port="5432", verbose=False)
tm.add_connection("fly_booking", database="fly_booking_db")
tm.add_connection("hotel_booking", database="hotel_booking_db")
tm.add_connection("account", database="account_db")


def decrease_money(conn, money):
    account_cursor = conn.cursor()
    account_query = "UPDATE account SET amount = amount - %s WHERE client_name = 'Roman Vey';"
    account_data = (money, )
    account_cursor.execute(account_query, account_data)

def book_hotel(conn):
    hotel_cursor = conn.cursor()
    hotel_query = "INSERT INTO hotel_booking (client_name, hotel_name, arrival, departure) VALUES (%s, %s, NOW(), NOW());"
    hotel_data = ("Roman Vey", "Nice Hotel")
    hotel_cursor.execute(hotel_query, hotel_data)


tm.create_transaction("book_hotel", ["hotel_booking", "account"])
tm.add_to_transaction("book_hotel", "hotel_booking", book_hotel, comment="Book hotel")
tm.add_to_transaction("book_hotel", "account", decrease_money, (300, ), comment="Take 300$")
tm.run_transaction("book_hotel")