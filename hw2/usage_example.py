from map_reduce import MapReduce

values_1 = [(10, "Roma"), (10, "Andrew"), (3, "Sofiya")]
values_2 = [(10, "Vasya"), (4, "Max"), (3, "Sofiya")]
values_3 = [(4, "Andrew")]
all_values = [(10, "Roma"), (10, "Andrew"), (3, "Sofiya"), (10, "Vasya"), (4, "Max"), (3, "Sofiya"), (4, "Andrew")]

def custom_map(data):
    d = dict()
    for key, value in data:
        if key not in d:
            d[key] = [value]
        else:
            d[key].append(value)

    out = []
    for key in d:
        out.append((key, len(d[key])))
    return out



def custom_reduce(data):
    d = dict()
    for key, value in data:
        if key not in d:
            d[key] = value
        else:
            d[key] += value

    out = []
    for key in d:
        out.append((key, d[key]))
    return out


## Same calls
mr_1 = MapReduce(verbose=False)
mr_1.map_one(custom_map, values_1)
mr_1.map_one(custom_map, values_2)
mr_1.map_one(custom_map, values_3)
print(mr_1.reduce(custom_reduce))


mr_2 = MapReduce(verbose=False)
mr_2.map(custom_map, all_values, 3)
print(mr_2.reduce(custom_reduce))

mr_3 = MapReduce(verbose=True)
print(mr_3.map_reduce(custom_map, custom_reduce, all_values, 3))
