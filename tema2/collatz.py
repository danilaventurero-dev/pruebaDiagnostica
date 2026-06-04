import time

def collatz_steps(n):
    steps = 0

    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1

        steps += 1

    return steps


LIMIT = 100000

start = time.perf_counter()

total_steps = 0

for i in range(1, LIMIT + 1):
    total_steps += collatz_steps(i)

end = time.perf_counter()

elapsed_ms = (end - start) * 1000

print(f"Tiempo: {elapsed_ms:.2f} ms")
print(f"Pasos totales: {total_steps}") 