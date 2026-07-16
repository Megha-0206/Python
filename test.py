l = [1, 2, 3, 2, 4, 3, 5]

i = 0
while i < len(l):
    j = i + 1
    while j < len(l):
        if l[i] == l[j]:
            del l[j]
        
    i += 1

print(l)