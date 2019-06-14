seq = range(10)
print(type(seq))
print(list(seq[0:]))
print(len(seq))
for i in seq:
    print(i, end=' ')
else:
    print()
print('ok')

for i in range(0, -10, -1):
    print(i, end=' ')
else:
    print()


for i in range(-10, 0, 1):
    print(i, end=' ')
else:
    print()

for i in range(0, 10, 2):
    print(i, end=' ')
else:
    print()