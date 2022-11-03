def decimal2binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

a = int(input())

print(decimal2binary(a))
print(decimal2binary(a)[7] + 1)

