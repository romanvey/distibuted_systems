import sys
import dill


class Node:
    def __init__(self):
        self.func = None
        self.values = None
    
    def listen(self):
        while True:
            ser_data = sys.stdin.buffer.raw.read()
            try:
                self.func, self.values =  dill.loads(ser_data)
            except Exception as e: continue
            else: break

        # out = [self.func(*row) for row in self.values]
        out = self.func(self.values)
        sys.stdout.buffer.write(dill.dumps(out))




node = Node()
node.listen()