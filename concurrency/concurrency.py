# threads
import threading
import time

results = {}
def long_square(num, results):
    time.sleep(1)
    results[num] = num**2

[long_square(n, results) for n in range(10)]

# create threads
t1 = threading.Thread(target=long_square, args=(1, results))
t2 = threading.Thread(target=long_square, args=(1, results))

# start threads
t1.start()
t2.start()

# join threads
t1.join()
t2.join()

print(results)

# typically add to list
threads = [threading.Thread(target=long_square(n, results)) for n in range(0, 5)]
[t.start() for t in threads]
[t.join for t in threads]
print(results)
