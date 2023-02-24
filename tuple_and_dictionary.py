t = (1, 2, 3, 1, 2, 1, 1, 4, 4)
count = t.count(1)
print(count)
index = t.index(2)
print(index)
index = t.index(2, 3, 5)
print(index)

s = sum(t)
print("Sum is", s)
print("Maximum in the tuple", max(t))
print("Minimum in the tuple", min(t))
a = [2, 4, 5]
print(sorted(a))
a.sort()
d1 = dict()
d2 = {}
print(type(d1))
print(type(d2))


student = {
    "name": "ABC",
    "age": 24,
    "address": "Kalanki"
}

students = [
{
    "name": "ABC",
    "age": 24,
    "address": "Kalanki"
},
    {
    "name": "ABC",
    "age": 24,
    "address": "Kalanki"
}

]

s = dict(name="ABC", address="Kalanki")
print("Result of dictionary", s.get("fkbsdkjfds"))