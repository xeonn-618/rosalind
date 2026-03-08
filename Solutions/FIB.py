def fib_rabbits(months, k_pairs):
    if months <= 1 or months == 2:
        return 1
    return (fib_rabbits(months-1,k_pairs)) + (fib_rabbits(months-2,k_pairs)*k_pairs)

max_months = 10
pairs = 1

for i in range(1, max_months+1):
    print(f"Month {i}: Rabbits {fib_rabbits(i,pairs)}")