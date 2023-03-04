a = "Python + is + an + awesome + language"
l = a.split("+")
l = [i.strip() for i in l]
print(l)
s = " ".join(l)
print(s)
