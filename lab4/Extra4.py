import time
import Main_task, Extra1, Extra2, Extra3


def benchmark(script):
    start_time = time.perf_counter()
    for i in range(100):
        script.start()
    end_time = time.perf_counter()

    return f"{end_time - start_time:.3f} сек"

print('> Main', benchmark(Main_task))
print('> Lib', benchmark(Extra1))
print('> Regex', benchmark(Extra2))
print('> Giga-parser', benchmark(Extra3))
