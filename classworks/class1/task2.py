vowels = ['a', 'e', 'i', 'o', 'u']
s = input("Enter the desired alphabet ")
if s.lower() in vowels:
    print(f"{s} is a vowel")
else:
    print(f"{s} is a consonant")
