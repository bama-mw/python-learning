var_array = [i for i in range(101)]

total = 0
count = 0

for value in var_array:
    total += value
    count += 1

if count > 0:
    result = total // count
else:
    result = 0

print(f"Hasil rata-rata: {result}")