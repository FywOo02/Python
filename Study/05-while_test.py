# 100以内偶数求和
result = 0
i = 0
while i <= 100:
    if i % 2 == 0:
        result += i
    i += 1
print(result)