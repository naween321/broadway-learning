def char_count_dict(s):
    d = dict()
    for each in s:
        if each not in d:
            d.update({each: s.count(each)})
    return d


r = char_count_dict("broadway")
print(r)
