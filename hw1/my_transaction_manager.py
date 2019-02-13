import psycopg2


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


    def add_to_transaction(self, transaction_name, conn_name, func, args=None, comment=None):
        if transaction_name in self.transactions: self.transactions[transaction_name] += [(conn_name, func, args, comment)]
        else: self.transactions[transaction_name] = [(conn_name, func, args, comment)]


    def remove_transaction(self, transaction_name):
        if transaction_name in self.transactions: 
            del(self.transactions[transaction_name])
        else:
            print("No such transaction")


    def __del__(self):
        for conn in self.connections:
            self.connections[conn].close()
        if self.verbose: print("All connections closed")


    def close(self): del(self)


    def _rollback(self, transaction_name):
        failed = False
        for conn, _, _, _ in self.transactions[transaction_name]:
            try:
                self.connections[conn].rollback()
            except (Exception, psycopg2.Error) as error:
                print("Error with PostgreSQL", error)
                failed = True
        if not failed: print("Transaction rolled back")


    def _commit(self, transaction_name):
        failed = False
        for conn, _, _, _ in self.transactions[transaction_name]:
            try:
                self.connections[conn].commit()
            except (Exception, psycopg2.Error) as error:
                print("Error with PostgreSQL", error)
                failed = True
        if not failed: print("Transaction commited")


    def run_transaction(self, transaction_name):
        if transaction_name not in self.transactions: 
            print("No such transaction")
            return
        need_rollback = False
        tmp_cursors= []
        for connection, func, args, comment in self.transactions[transaction_name]:
            if comment: print(comment)
            if connection not in self.connections:
                print("No such connection:", connection)
                need_rollback = True
                break
            cursor = self.connections[connection].cursor()
            tmp_cursors.append(cursor)
            try:
                if args is not None: func(cursor, *args)
                else: func(cursor)
            except  (Exception, psycopg2.Error) as error :
                print ("Error with PostgreSQL", error)
                need_rollback = True
                break
            
        if need_rollback: self._rollback(transaction_name)
        else: self._commit(transaction_name)
        for cursor in tmp_cursors: cursor.close()