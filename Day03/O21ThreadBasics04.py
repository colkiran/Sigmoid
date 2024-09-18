
import time
import threading
import concurrent.futures

def doJob(secs):
    print(f"Sleeping for {secs} seconds ....{threading.current_thread().name}")
    time.sleep(secs)
    print(f'Just woke up.....{threading.current_thread().name}')

st = time.perf_counter()
with concurrent.futures.ThreadPoolExecutor() as executor:
    thrd1 = executor.submit(doJob, 2)
    thrd2 = executor.submit(doJob, 2)
    thrd3 = executor.submit(doJob, 2)

    res1 = thrd1.result()
    res2 = thrd2.result()
    res3 = thrd3.result()

et = time.perf_counter()
print(f"The total time taken {et - st}")
