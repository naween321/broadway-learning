def combine_dict(d1, d2):
    result = dict()
    keys = set(d1.keys()).union(d2.keys())
    for key in keys:
        if key in d1 and key in d2:
            result.update({key: d1[key] + d2[key]})
        elif key in d1:
            result.update({key: d1[key]})
        else:
            result.update({key: d2[key]})
    return result


dictionary1 = {'a': 100, 'b': 200, 'c': 300}
dictionary2 = {'a': 300, 'b': 200, 'd': 400}

r = combine_dict(dictionary1, dictionary2)
print(r)
