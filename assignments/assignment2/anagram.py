def is_anagram(s1, s2):
    if len(s1) == len(s2):
        if set(s1) == set(s2):
            return "Is Anagram"
    return "Not Anagram"


r = is_anagram("silent", "listen")
print(r)
