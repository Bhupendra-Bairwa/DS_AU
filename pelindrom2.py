word = input("Enter the word: ")
rev = ""
for char in word:
    rev = char+rev
if rev ==word:
    print("pelindrom")
else:
    print("not palendrom")