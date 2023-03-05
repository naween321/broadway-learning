def join_str(a):
    l = a.split("+")
    l = [i.strip() for i in l]
    print(l)
    s = " ".join(l)
    return s


r = join_str("Python + is + an + awesome + language")
print(r)
