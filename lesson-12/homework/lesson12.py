import threading

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def check_primes_in_range(start, end, result_list):
    primes = [n for n in range(start, end + 1) if is_prime(n)]
    result_list.extend(primes)

def threaded_prime_checker(start, end, num_threads=4):
    threads = []
    result_list = []
    result_lock = threading.Lock()
    step = (end - start + 1) // num_threads

    def worker(s, e):
        local_primes = [n for n in range(s, e + 1) if is_prime(n)]
        with result_lock:
            result_list.extend(local_primes)

    for i in range(num_threads):
        s = start + i * step
        e = start + (i + 1) * step - 1 if i < num_threads - 1 else end
        t = threading.Thread(target=worker, args=(s, e))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    return sorted(result_list)



print("Primes between 1 and 100:", threaded_prime_checker(1, 100, num_threads=4))

import threading
from collections import Counter

def process_lines(lines, counter, lock):
    local_counter = Counter()
    for line in lines:
        words = line.strip().split()
        local_counter.update(words)
    with lock:
        counter.update(local_counter)

def threaded_word_count(file_path, num_threads=4):
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    threads = []
    counter = Counter()
    lock = threading.Lock()
    step = len(lines) // num_threads

    for i in range(num_threads):
        start = i * step
        end = (i + 1) * step if i < num_threads - 1 else len(lines)
        t = threading.Thread(target=process_lines, args=(lines[start:end], counter, lock))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    return counter

summary = threaded_word_count("test.txt", num_threads=4)
print("Word occurrences:", summary)
