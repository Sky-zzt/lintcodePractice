a = [1, 2, 3, 4, 5, 6, 7, 8]
print(id(a))
print(id(a[:]))
for i in a[:]:
    if i > 5:
        pass
    else:
        a.remove(i)
    print(a)
print('-----------')
print(id(a))
