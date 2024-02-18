purse = dict()
purse["money"] = 12
purse["candy"] = 3
purse["tissues"] = 75
print(purse)
print(purse["candy"])
purse["candy"] = purse["candy"] + 2
print(purse)

#count
ccc = dict()
ccc["csev"] = 1
ccc["cwen"] = 1
print(ccc)
ccc["cwen"] = ccc["cwen"] + 1
print(ccc)

counts = dict()
names = ["csev", "cwen", "csev", "zqian", "cwen"]
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
    #or
    counts[name] = counts.get(name, 0) + 1
print(counts)     

#counting words
counts = dict()
print("Enter a line of test: ")
line = input()
words = line.split()
print("Words: ", words)
print("Counting...")
for word in words:
    counts[word] = counts.get(word, 0) + 1
print("Counts", counts)

counts = {"chuck" : 1, "fred" : 42, "jan" : 100}
for key in counts:
    print(key, counts[key])
print(list(counts))
print(counts.keys())
print(counts.values())
print(counts.items())

for aaa, bbb in counts.items():
    print(aaa, bbb)


import string

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

counts = dict()
for line in fhand:
    line = line.rstrip()
    line = line.translate(line.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

print(counts)

