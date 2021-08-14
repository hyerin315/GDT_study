num = int(input("원하는 단은: "))

for i in range(1, 10):
    print(num, "*", i, "=", num * i)
print("="*10)

i = 1
while i < 10:
    print(num, "*", i, "=", num * i)
    i += 1