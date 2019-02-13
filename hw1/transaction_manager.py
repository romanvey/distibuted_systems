import psycopg2
import random

class TransactionManager:
    def __init__(self, user="postgres", password="postgres", host="localhost", port="5432", database="postgres", verbose=True):
        self.connections = dict()
        self.transactions = dict()
        self.verbose = verbose
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.database = database


    def add_connection(self, connection_name, user=None, password=None, host=None, port=None, database=None):
        if user is None: user = self.user
        if password is None: password = self.password
        if host is None: host = self.host
        if port is None: port = self.port
        if database is None: database = self.database

        if connection_name in self.connections:
            print("Connection already exists")
            return
        try:
            connection = psycopg2.connect(user = user,
                                            password = password,
                                            host = host,
                                            port = port,
                                            database = database)
            connection.autocommit = False
        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)
            return
        if connection is not None:
            self.connections[connection_name] = connection


    def remove_connection(self, connection_name):
        if connection_name in self.connections:
            self.connections[connection_name].close()
            del(self.connections[connection_name])
        else:
            print("No such connection")


    def get_connection(self, connection_name):
        if connection_name in self.connections:
            return self.connections[connection_name]
        else:
            print("No such connection")



    def __del__(self):
        for conn in self.connections:
            self.connections[conn].close()
        if self.verbose: print("All connections closed")


    def close(self): del(self)


    def create_transaction(self, transaction_name, connections):
        if transaction_name in self.transactions:
            print("Transaction already exists")
            return
        for connection in connections:
            if connection not in self.connections:
                print("No such connection:", connection)
                return
        id = random.randint(1,10**8)
        for connection in connections:
            self.connections[connection].tpc_begin(self.connections[connection].xid(42, str(id), connection))
        self.transactions[transaction_name] = (connections, [])


    def add_to_transaction(self, transaction_name, connection_name, func, args=None, comment=None):
        if transaction_name not in self.transactions:
            print("No such transaction")
            return
        if connection_name not in self.transactions[transaction_name][0]:
            print("No such connection in transaction:", connection_name)
            return
        self.transactions[transaction_name][1].append((connection_name, func, args, comment))


    def run_transaction(self, transaction_name):
        if transaction_name not in self.transactions:
            print("No such transaction")
            return
        for connection_name, func, args, comment in self.transactions[transaction_name][1]:
            try:
                if comment: print(comment)
                conn = self.connections[connection_name]
                if args: func(conn, *args)
                else: func(conn)
            except (Exception, psycopg2.Error) as error:
                print("Error with PostgreSQL", error)  
                return

        try:
            for connection in self.transactions[transaction_name][0]:
                self.connections[connection].tpc_prepare()
        except (Exception, psycopg2.Error) as error:
            for connection in self.transactions[transaction_name][0]:
                self.connections[connection].tpc_rollback()
            print("Error with PostgreSQL", error)
        else:
            pass
            # for connection in self.transactions[transaction_name][0]:
            #     self.connections[connection].tpc_commit()