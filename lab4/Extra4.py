import time

start_time = time.perf_counter()

for i in range(100):
    import Main_task
end_time = time.perf_counter()
print(f"Основа - {end_time - start_time:.8f} сек")

start_time = time.perf_counter()
for i in range(100):
    import Extra1
end_time = time.perf_counter()
print(f"Доп 1  - {end_time - start_time:.8f} сек")

start_time = time.perf_counter()
for i in range(100):
    import Extra2
end_time = time.perf_counter()
print(f"Доп 2  - {end_time - start_time:.8f} сек")

start_time = time.perf_counter()
for i in range(100):
    import Extra3
end_time = time.perf_counter()
print(f"Доп 3  - {end_time - start_time:.8f} сек")