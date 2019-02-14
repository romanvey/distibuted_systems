import subprocess
import dill
import uuid


class MapReduce:
    def __init__(self, verbose=False):
        self.verbose = verbose
        self.data = []


    def map(self, func, data, nodes):
        part = len(data) // nodes
        for i in range(nodes):
            if i != nodes - 1: self.map_one(func, data[i*part:(i+1)*part])
            else: self.map_one(func, data[i*part:])


    def map_one(self, func, data):
        id = uuid.uuid4()
        process = subprocess.Popen(["python", "node.py"], stdout=subprocess.PIPE, stdin=subprocess.PIPE)
        
        to_send = dill.dumps((func, data))
        process.stdin.write(to_send)
        process.stdin.close()

        out = dill.loads(process.stdout.read())
        if self.verbose:
            print("Node {} output:".format(id))
            print(out)
        self.data += out


    def reduce(self, func):
        if not self.data:
            print("Need map call before!")
            return
        out = func(self.data)
        self.data = []
        return out


    def map_reduce(self, map_func, reduce_func, data, nodes):
        self.map(map_func, data, nodes)
        return self.reduce(reduce_func)