data = ["apple", "BANANA", "cherry", "DATE", "elderberry"]

for x in data:
    if x.isupper():
        continue
    else:
        print(x.title())